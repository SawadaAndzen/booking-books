from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
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
    bookings = Booking.objects.filter(user = request.user)
    print(timezone.now())
    
    for booking in bookings:
        if booking.expires < timezone.now():
            book = booking.book
            book.quantity += booking.quantity
            book.save()
            
            booking.status = "Expired"
            booking.save()
            
    bookings = Booking.objects.filter(user=request.user)
    
    return render(request, 'profile.html', {'bookings': bookings})


def read_books_list(request):
    books = Book.objects.all().filter(quantity__gt = 0)
    
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

@login_required
def add_book(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = BookForm(request.POST)
        
            if form.is_valid():
                form.save()
            
                return redirect('books_list')
        
        else:
            form = BookForm()

        return render(request, 'add_book.html', {'form': form})


@login_required
def create_booking(request, book_id):
    book = get_object_or_404(Book, id = book_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            quantity_to_book = form.cleaned_data['quantity']

            if book.quantity >= quantity_to_book:
                booking = form.save(commit = False)
                booking.user = request.user
                booking.book = book
                booking.status = "Active"
                booking.expires = timezone.now() + timedelta(days = 3)

                book.quantity -= quantity_to_book
                book.save()
                booking.save()

                return redirect('profile')
            else:
                form.add_error('quantity', f'Not enough copies available. Only {book.quantity} left.')  # Add an error if not enough copies

    else:
        form = BookingForm(initial={'book': book})

    return render(request, 'create_booking.html', {'form': form, 'book': book})


@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id = booking_id)
    
    if request.method == 'POST':
        booking.delete()

        return redirect('profile')

    return render(request, 'confirm_delete.html', {'booking': booking})


@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    
    if request.method == 'POST':
        book = booking.book
        book.quantity += booking.quantity
        book.save()
        
        booking.status = "Cancelled"
        booking.save()

        return redirect('profile')

    return render(request, 'confirm_cancel.html', {'booking': booking})