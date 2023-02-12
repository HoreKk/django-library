from django.shortcuts import  render, redirect
from .forms import NewUserForm, SessionForm
from django.contrib.auth import login
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import CustomUser, Book, Library, Author, Editor, Collection, Genre, Reading_Group, Session, Reading_Group_User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView, View
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={ "register_form": form })


class HomeView(LoginRequiredMixin, TemplateView):
	template_name = 'home.html'

## Client Views ##

class BookListView(LoginRequiredMixin, ListView):
	model = Book
	template_name = 'client/book_list.html'

	def get_queryset(self):
		query = self.request.GET.get("q")
		if query is not None and query != '':
			object_list = Book.objects.filter(title__icontains=query)
		else:
			object_list = Book.objects.all()
		return object_list

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		tmpQuery = self.request.GET.get("q")
		if tmpQuery is not None:
			context['query'] = tmpQuery
		return context

class BookDetailView(LoginRequiredMixin, DetailView):
	model = Book
	template_name = 'client/book_detail.html'

class ReadingGroupListView(LoginRequiredMixin, ListView):
	model = Reading_Group
	template_name = 'client/reading_group_list.html'

class ReadingGroupSessionListView(LoginRequiredMixin, ListView):
	model = Session
	template_name = 'client/reading_group_session_list.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		new_object_list = []
		for session in context['object_list']:
			reading_group_user = Reading_Group_User.objects.filter(session=session.id, user=self.request.user.id).first()
			if reading_group_user is not None:
				session.reading_group_user = reading_group_user
			new_object_list.append(session)
		context['object_list'] = new_object_list
		return context

class ReadingGroupSessionUserCreateView(LoginRequiredMixin, View):
	def post(self, request, *args, **kwargs):
		session = get_object_or_404(Session, id=self.kwargs['pk_session'])
		user = get_object_or_404(CustomUser, id=self.kwargs['pk_user'])
		Reading_Group_User(session=session, user=user, status= 'pending').save()
		return HttpResponseRedirect(reverse_lazy('reading_group_session_list', kwargs={'pk': session.reading_group.id }))

## Back Office Views ##

# Books CRUD
class BoBookListView(UserPassesTestMixin, ListView):
	model = Book
	template_name = 'back/books/list.html'

	def test_func(self):
		return self.request.user.library is not None

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['book_fields'] = [f.name for f in Book._meta.get_fields()]
		return context

class BoBookCreateView(LoginRequiredMixin, CreateView):
	model = Book
	fields = ['title', 'cover', 'author', 'editor', 'collection', 'genre']
	template_name = 'back/books/edit.html'
	success_url = '/bo/books'

	def form_valid(self, form):
		library = get_object_or_404(Library, name=self.request.user.library)
		form.instance.library = library
		return super(BoBookCreateView, self).form_valid(form)

class BoBookUpdateView(LoginRequiredMixin, UpdateView):
	model = Book
	fields = ['title', 'cover', 'author', 'editor', 'collection', 'genre']
	template_name = 'back/books/edit.html'
	success_url = '/bo/books'

class BoBookDeleteView(LoginRequiredMixin, DeleteView):
	model = Book
	success_url = reverse_lazy('book_list')


# Authors CRUD
class BoAuthorListView(UserPassesTestMixin, ListView):
	model = Author
	template_name = 'back/authors/list.html'

	def test_func(self):
		return self.request.user.library is not None

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['author_fields'] = [f.name for f in Author._meta.get_fields()]
		return context

class BoAuthorCreateView(LoginRequiredMixin, CreateView):
	model = Author
	fields = ['first_name', 'last_name']
	template_name = 'back/authors/edit.html'
	success_url = '/bo/authors'

class BoAuthorUpdateView(LoginRequiredMixin, UpdateView):
	model = Author
	fields = ['first_name', 'last_name']
	template_name = 'back/authors/edit.html'
	success_url = '/bo/authors'

class BoAuthorDeleteView(LoginRequiredMixin, DeleteView):
	model = Author
	success_url = reverse_lazy('bo_author_list')


# Editors CRUD
class BoEditorListView(UserPassesTestMixin, ListView):
	model = Editor
	template_name = 'back/editors/list.html'

	def test_func(self):
		return self.request.user.library is not None

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['editor_fields'] = [f.name for f in Editor._meta.get_fields()]
		return context

class BoEditorCreateView(LoginRequiredMixin, CreateView):
	model = Editor
	fields = ['name']
	template_name = 'back/editors/edit.html'
	success_url = '/bo/editors'

class BoEditorUpdateView(LoginRequiredMixin, UpdateView):
	model = Editor
	fields = ['name']
	template_name = 'back/editors/edit.html'
	success_url = '/bo/editors'

class BoEditorDeleteView(LoginRequiredMixin, DeleteView):
	model = Editor
	success_url = reverse_lazy('bo_editor_list')


# Collections CRUD
class BoCollectionListView(UserPassesTestMixin, ListView):
	model = Collection
	template_name = 'back/collections/list.html'

	def test_func(self):
		return self.request.user.library is not None

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['collection_fields'] = [f.name for f in Collection._meta.get_fields()]
		return context

class BoCollectionCreateView(LoginRequiredMixin, CreateView):
	model = Collection
	fields = ['name', 'color']
	template_name = 'back/collections/edit.html'
	success_url = '/bo/collections'

class BoCollectionUpdateView(LoginRequiredMixin, UpdateView):
	model = Collection
	fields = ['name', 'color']
	template_name = 'back/collections/edit.html'
	success_url = '/bo/collections'

class BoCollectionDeleteView(LoginRequiredMixin, DeleteView):
	model = Collection
	success_url = reverse_lazy('bo_collection_list')


# Collections CRUD
class BoGenreListView(UserPassesTestMixin, ListView):
	model = Genre
	template_name = 'back/genres/list.html'

	def test_func(self):
		return self.request.user.library is not None

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['genre_fields'] = [f.name for f in Genre._meta.get_fields()]
		return context

class BoGenreCreateView(LoginRequiredMixin, CreateView):
	model = Genre
	fields = ['name']
	template_name = 'back/genres/edit.html'
	success_url = '/bo/genres'

class BoGenreUpdateView(LoginRequiredMixin, UpdateView):
	model = Genre
	fields = ['name']
	template_name = 'back/genres/edit.html'
	success_url = '/bo/genres'

class BoGenreDeleteView(LoginRequiredMixin, DeleteView):
	model = Genre
	success_url = reverse_lazy('bo_genre_list')


# ReadingGroup CRUD
class BoReadingGroupListView(UserPassesTestMixin, ListView):
	model = Reading_Group
	template_name = 'back/reading-groups/list.html'

	def test_func(self):
		return self.request.user.library is not None

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['reading_group_fields'] = [f.name for f in Reading_Group._meta.get_fields()]
		return context

class BoReadingGroupCreateView(LoginRequiredMixin, CreateView):
	model = Reading_Group
	fields = ['name']
	template_name = 'back/reading-groups/edit.html'
	success_url = '/bo/reading-groups'

class BoReadingGroupUpdateView(LoginRequiredMixin, UpdateView):
	model = Reading_Group
	fields = ['name']
	template_name = 'back/reading-groups/edit.html'
	success_url = '/bo/reading-groups'


class BoReadingGroupDeleteView(LoginRequiredMixin, DeleteView):
	model = Reading_Group
	success_url = reverse_lazy('bo_reading_group_list')


# ReadingGroup Sessions CRUD
class BoReadingGroupSessionsView(LoginRequiredMixin, ListView):
	model = Session
	fields = ['date']
	template_name = 'back/reading-groups/sessions/list.html'
	
	def get_queryset(self):
		return Session.objects.filter(reading_group=self.kwargs['pk_reading_group'])

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['session_fields'] = [f.name for f in Session._meta.get_fields()]
		context['reading_group'] = Reading_Group.objects.get(id=self.kwargs['pk_reading_group'])
		new_object_list = []
		for session in context['object_list']:
			reading_group_users = Reading_Group_User.objects.filter(session=session.id)
			if reading_group_users is not None:
				session.reading_group_users = reading_group_users
			new_object_list.append(session)
		context['object_list'] = new_object_list
		return context

class BoReadingGroupSessionUsersView(LoginRequiredMixin, ListView):
	model = Reading_Group_User
	fields = ['session', 'user', 'status']
	template_name = 'back/reading-groups/sessions/users.html'
	
	def get_queryset(self):
		return Reading_Group_User.objects.filter(session=self.kwargs['pk_session'])

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['reading_group_user_fields'] = [f.name for f in Reading_Group_User._meta.get_fields()]
		return context

class BoReadingGroupSessionUserUpdateView(LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):
		reading_group_user = get_object_or_404(Reading_Group_User, id=self.kwargs['pk_reading_group_user'])
		reading_group_user.status = self.kwargs['status']
		reading_group_user.save()
		return HttpResponseRedirect(reverse_lazy('bo_reading_group_session_user_list', kwargs={'pk_reading_group': reading_group_user.session.reading_group.id, 'pk_session': reading_group_user.session.id }))

class BoReadingGroupSessionCreateView(LoginRequiredMixin, CreateView):
	form_class = SessionForm
	template_name = 'back/reading-groups/sessions/edit.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['reading_group'] = Reading_Group.objects.get(id=self.kwargs['pk_reading_group'])
		return context

	def form_valid(self, form):
		reading_group = get_object_or_404(Reading_Group, id=self.kwargs['pk_reading_group'])
		form.instance.reading_group = reading_group
		return super(BoReadingGroupSessionCreateView, self).form_valid(form)

	def get_success_url(self) -> str:
		return reverse_lazy('bo_reading_group_session_list', kwargs={'pk_reading_group': self.kwargs['pk_reading_group'] })

class BoReadingGroupSessionUpdateView(LoginRequiredMixin, UpdateView):
	model = Session
	slug_field = 'id'
	slug_url_kwarg = 'pk_session'
	fields = ['date']
	template_name = 'back/reading-groups/sessions/edit.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['reading_group'] = Reading_Group.objects.get(id=self.kwargs['pk_reading_group'])
		return context

	def get_success_url(self) -> str:
		return reverse_lazy('bo_reading_group_session_list', kwargs={'pk_reading_group': self.kwargs['pk_reading_group'] })

class BoReadingGroupSessionDeleteView(LoginRequiredMixin, DeleteView):
	model = Session
	slug_field = 'id'
	slug_url_kwarg = 'pk_session'

	def get_success_url(self) -> str:
		return reverse_lazy('bo_reading_group_session_list', kwargs={'pk_reading_group': self.kwargs['pk_reading_group'] })