from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['id','title', 'author', 'description', 'genre', 'pages', 'library', 'price', 'quantity']