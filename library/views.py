from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
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


# Books CRUD
class BookListView(UserPassesTestMixin, ListView):
	model = Book
	template_name = 'back/books/list.html'

	def test_func(self):
		return self.request.user.library is not None

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['book_fields'] = [f.name for f in Book._meta.get_fields()]
		return context

class BookCreateView(LoginRequiredMixin, CreateView):
	model = Book
	fields = ['title', 'author', 'editor', 'collection', 'genre']
	template_name = 'back/books/edit.html'
	success_url = '/books'

	def form_valid(self, form):
		library = get_object_or_404(Library, name=self.request.user.library)
		form.instance.library = library
		return super(BookCreateView, self).form_valid(form)

class BookUpdateView(LoginRequiredMixin, UpdateView):
	model = Book
	fields = ['title', 'author', 'editor', 'collection', 'genre']
	template_name = 'back/books/edit.html'
	success_url = '/books'

class BookDeleteView(LoginRequiredMixin, DeleteView):
	model = Book
	success_url = reverse_lazy('book_list')


# Authors CRUD
class AuthorListView(UserPassesTestMixin, ListView):
	model = Author
	template_name = 'back/authors/list.html'

	def test_func(self):
		return self.request.user.library is not None

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['author_fields'] = [f.name for f in Author._meta.get_fields()]
		return context

class AuthorCreateView(LoginRequiredMixin, CreateView):
	model = Author
	fields = ['first_name', 'last_name']
	template_name = 'back/authors/edit.html'
	success_url = '/authors'

class AuthorUpdateView(LoginRequiredMixin, UpdateView):
	model = Author
	fields = ['first_name', 'last_name']
	template_name = 'back/authors/edit.html'
	success_url = '/authors'

class AuthorDeleteView(LoginRequiredMixin, DeleteView):
	model = Author
	success_url = reverse_lazy('lib_author_list')


# Editors CRUD
class EditorListView(UserPassesTestMixin, ListView):
	model = Editor
	template_name = 'back/editors/list.html'

	def test_func(self):
		return self.request.user.library is not None

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['editor_fields'] = [f.name for f in Author._meta.get_fields()]
		return context

class EditorCreateView(LoginRequiredMixin, CreateView):
	model = Editor
	fields = ['first_name', 'last_name']
	template_name = 'back/editors/edit.html'
	success_url = '/editors'

class EditorUpdateView(LoginRequiredMixin, UpdateView):
	model = Editor
	fields = ['first_name', 'last_name']
	template_name = 'back/editors/edit.html'
	success_url = '/editors'

class EditorDeleteView(LoginRequiredMixin, DeleteView):
	model = Editor
	success_url = reverse_lazy('lib_editor_list')


# Collections CRUD
class CollectionListView(UserPassesTestMixin, ListView):
	model = Collection
	template_name = 'back/collections/list.html'

	def test_func(self):
		return self.request.user.library is not None

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['collection_fields'] = [f.name for f in Collection._meta.get_fields()]
		return context

class CollectionCreateView(LoginRequiredMixin, CreateView):
	model = Collection
	fields = ['name', 'color']
	template_name = 'back/collections/edit.html'
	success_url = '/collections'

class CollectionUpdateView(LoginRequiredMixin, UpdateView):
	model = Collection
	fields = ['name', 'color']
	template_name = 'back/collections/edit.html'
	success_url = '/collections'

class CollectionDeleteView(LoginRequiredMixin, DeleteView):
	model = Collection
	success_url = reverse_lazy('lib_collection_list')


# Collections CRUD
class GenreListView(UserPassesTestMixin, ListView):
	model = Genre
	template_name = 'back/genres/list.html'

	def test_func(self):
		return self.request.user.library is not None

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['genre_fields'] = [f.name for f in Genre._meta.get_fields()]
		return context

class GenreCreateView(LoginRequiredMixin, CreateView):
	model = Genre
	fields = ['name']
	template_name = 'back/genres/edit.html'
	success_url = '/genres'

class GenreUpdateView(LoginRequiredMixin, UpdateView):
	model = Genre
	fields = ['name']
	template_name = 'back/genres/edit.html'
	success_url = '/genres'

class GenreDeleteView(LoginRequiredMixin, DeleteView):
	model = Genre
	success_url = reverse_lazy('lib_genre_list')