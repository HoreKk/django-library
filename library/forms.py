from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Session

from django.forms import ModelForm
from .models import Book
from django.contrib.auth import get_user_model

User = get_user_model()

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	
	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2", "library")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class BookForm(ModelForm):
		class Meta:
			model = Book
			fields = ['title', 'author', 'cover', 'editor', 'collection', 'genre', 'library']

class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }