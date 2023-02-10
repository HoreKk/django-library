from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Book, Library, Author, Editor, Collection, Genre
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy


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

class BookDetailView(LoginRequiredMixin, DetailView):
	model = Book
	template_name = 'client/book_detail.html'

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
		context['editor_fields'] = [f.name for f in Author._meta.get_fields()]
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