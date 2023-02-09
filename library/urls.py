"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('__reload__/', include("django_browser_reload.urls")),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.register_request, name="register"),
    path('', views.HomeView.as_view(), name='home'),
    path('books', views.BookListView.as_view(), name='lib_book_list'),
    path('book', views.BookCreateView.as_view(), name='lib_book_create'),
    path('book/<slug:pk>', views.BookUpdateView.as_view(), name='lib_book_detail'),
    path('book/<slug:pk>/delete', views.BookDeleteView.as_view(), name='lib_book_delete'),
    path('authors', views.AuthorListView.as_view(), name='lib_author_list'),
    path('author', views.AuthorCreateView.as_view(), name='lib_author_create'),
    path('author/<slug:pk>', views.AuthorUpdateView.as_view(), name='lib_author_detail'),
    path('author/<slug:pk>/delete', views.AuthorDeleteView.as_view(), name='lib_author_delete'),
    path('editors', views.EditorListView.as_view(), name='lib_editor_list'),
    path('editor', views.EditorCreateView.as_view(), name='lib_editor_create'),
    path('editor/<slug:pk>', views.EditorUpdateView.as_view(), name='lib_editor_detail'),
    path('editor/<slug:pk>/delete', views.EditorDeleteView.as_view(), name='lib_editor_delete'),
    path('collections', views.CollectionListView.as_view(), name='lib_collection_list'),
    path('collection', views.CollectionCreateView.as_view(), name='lib_collection_create'),
    path('collection/<slug:pk>', views.CollectionUpdateView.as_view(), name='lib_collection_detail'),
    path('collection/<slug:pk>/delete', views.CollectionDeleteView.as_view(), name='lib_collection_delete'),
    path('genres', views.GenreListView.as_view(), name='lib_genre_list'),
    path('genre', views.GenreCreateView.as_view(), name='lib_genre_create'),
    path('genre/<slug:pk>', views.GenreUpdateView.as_view(), name='lib_genre_detail'),
    path('genre/<slug:pk>/delete', views.GenreDeleteView.as_view(), name='lib_genre_delete'),
]
