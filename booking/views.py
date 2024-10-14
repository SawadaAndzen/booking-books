from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Book
from .forms import BookForm


def index(request):
    return render(request, 'index.html')


def read_books_list(request):
    books = Book.objects.all()
    
    return render(request, 'books_list.html', {'books': books})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('login')
    
    else:
        form = UserCreationForm()
    
    return render(request, 'auth/signup.html', {'form': form})


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('books_list')
        
    else:
        form = BookForm()

    return render(request, 'add_book.html', {'form': form})