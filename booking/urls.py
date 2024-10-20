from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('books/', views.read_books_list, name='books_list'),
    path('add-book/', views.add_book, name='add_book'),
    path('create-booking/<int:book_id>/', views.create_booking, name='create_booking'),
    path('about/', views.about, name='about'),
    path('profile/', views.read_profile, name='profile'),
    path('signup/', views.signup, name = 'signup'),
    path('booking/delete/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('booking/cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]