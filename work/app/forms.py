from django import forms
from django.contrib.auth.forms import UserCreationForm

from app.models import CustomUser

from app.models import Book


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'phone')

class bookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields="__all__"