"""borary URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('__reload__/', include("django_browser_reload.urls")),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.register_request, name="register"),
    path('', views.HomeView.as_view(), name='home'),

    ## Client Routes ##
    path('books', views.BookListView.as_view(), name='book_list'),
    path('book/<slug:pk>', views.BookDetailView.as_view(), name='book_detail'),
    
    ## Back Office Routes ##
    path('bo/books', views.BoBookListView.as_view(), name='bo_book_list'),
    path('bo/book', views.BoBookCreateView.as_view(), name='bo_book_create'),
    path('bo/book/<slug:pk>', views.BoBookUpdateView.as_view(), name='bo_book_detail'),
    path('bo/book/<slug:pk>/delete', views.BoBookDeleteView.as_view(), name='bo_book_delete'),
    path('bo/authors', views.BoAuthorListView.as_view(), name='bo_author_list'),
    path('bo/author', views.BoAuthorCreateView.as_view(), name='bo_author_create'),
    path('bo/author/<slug:pk>', views.BoAuthorUpdateView.as_view(), name='bo_author_detail'),
    path('bo/author/<slug:pk>/delete', views.BoAuthorDeleteView.as_view(), name='bo_author_delete'),
    path('bo/editors', views.BoEditorListView.as_view(), name='bo_editor_list'),
    path('bo/editor', views.BoEditorCreateView.as_view(), name='bo_editor_create'),
    path('bo/editor/<slug:pk>', views.BoEditorUpdateView.as_view(), name='bo_editor_detail'),
    path('bo/editor/<slug:pk>/delete', views.BoEditorDeleteView.as_view(), name='bo_editor_delete'),
    path('bo/collections', views.BoCollectionListView.as_view(), name='bo_collection_list'),
    path('bo/collection', views.BoCollectionCreateView.as_view(), name='bo_collection_create'),
    path('bo/collection/<slug:pk>', views.BoCollectionUpdateView.as_view(), name='bo_collection_detail'),
    path('bo/collection/<slug:pk>/delete', views.BoCollectionDeleteView.as_view(), name='bo_collection_delete'),
    path('bo/genres', views.BoGenreListView.as_view(), name='bo_genre_list'),
    path('bo/genre', views.BoGenreCreateView.as_view(), name='bo_genre_create'),
    path('bo/genre/<slug:pk>', views.BoGenreUpdateView.as_view(), name='bo_genre_detail'),
    path('bo/genre/<slug:pk>/delete', views.BoGenreDeleteView.as_view(), name='bo_genre_delete'),
    path('bo/reading-groups', views.BoReadingGroupListView.as_view(), name='bo_reading_group_list'),
    path('bo/reading-group', views.BoReadingGroupCreateView.as_view(), name='bo_reading_group_create'),
    path('bo/reading-group/<slug:pk>', views.BoReadingGroupUpdateView.as_view(), name='bo_reading_group_detail'),
    path('bo/reading-group/<slug:pk>/delete', views.BoReadingGroupDeleteView.as_view(), name='bo_reading_group_delete'),
    path('bo/reading-group/<slug:pk_reading_group>/sessions', views.BoReadingGroupSessionsView.as_view(), name='bo_reading_group_session_list'),
    path('bo/reading-group/<slug:pk_reading_group>/session', views.BoReadingGroupSessionCreateView.as_view(), name='bo_reading_group_session_create'),
    path('bo/reading-group/<slug:pk_reading_group>/session/<slug:pk_session>', views.BoReadingGroupSessionUpdateView.as_view(), name='bo_reading_group_session_detail'),
    path('bo/reading-group/<slug:pk_reading_group>/session/<slug:pk_session>/delete', views.BoReadingGroupSessionDeleteView.as_view(), name='bo_reading_group_session_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
