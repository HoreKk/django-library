from django.shortcuts import  render, redirect
from .forms import NewUserForm, BookForm
from django.contrib.auth import login
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from .models import Book

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


class BookListView(ListView):
	model = Book
	template_name = 'back/list_books.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['book_fields'] = [f.name for f in Book._meta.get_fields()]
		return context

class BookCreateView(CreateView):
	model = Book
	fields = ['title', 'author', 'editor', 'collection', 'genre', 'library']
	template_name = 'back/edit_book.html'
	redirect = 'book_list'

class BookUpdateView(UpdateView):
	model = Book
	fields = ['title', 'author', 'editor', 'collection', 'genre', 'library']
	template_name = 'back/edit_book.html'
	redirect = 'book_list'

def create_book(request):
	if request.method == "POST":
		form = BookForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Book created." )
			return redirect("list_books")
		messages.error(request, "Invalid fields.")
	form = BookForm()
	return render (request=request, template_name="back/create_book.html", context={ "create_book_form": form })