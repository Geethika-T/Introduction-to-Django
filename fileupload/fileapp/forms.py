from django import forms

from fileapp.models import Book


class bookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields="__all__"