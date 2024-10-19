from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import timedelta
from .models import Book, Booking
from .forms import BookForm, BookingForm, CustomSignUpForm


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


@login_required
def read_profile(request):
    bookings = Booking.objects.all().filter(user = request.user)
    
    return render(request, 'profile.html', {'bookings': bookings})


def read_books_list(request):
    books = Book.objects.all()
    
    return render(request, 'books_list.html', {'books': books})


def signup(request):
    if request.method == 'POST':
        form = CustomSignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('login')
    
    else:
        form = CustomSignUpForm()
    
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


@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.expires = booking.date + timedelta(days=3)
            booking.save()
            
            return redirect('profile')
        
    else:
        form = BookingForm()
        
    return render(request, 'create_booking.html', {'form': form})


@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    
    if request.method == 'POST':
        booking.delete()

        return redirect('profile')

    return render(request, 'confirm_delete.html', {'booking': booking})