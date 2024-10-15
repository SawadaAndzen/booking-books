from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('books/', views.read_books_list, name='books_list'),
    path('add-book/', views.add_book, name='add_book'),
    path('signup/', views.signup, name = 'signup')
]