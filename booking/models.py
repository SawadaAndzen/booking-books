from django.db import models
from django.contrib.auth.models import User


class Library(models.Model):
    id = models.PositiveIntegerField(auto_created = True, unique = True, primary_key = True)
    name = models.CharField(max_length = 50)
    desciption = models.TextField()
    adress = models.CharField(max_length = 150)
    start_work_time = models.TimeField()
    end_work_time = models.TimeField()
    
    def __str__(self):
        return f"{self.name} - ({self.start_work_time} - {self.end_work_time})"
    
    
class Author(models.Model):
    name = models.CharField(max_length = 50)
    surname = models.CharField(max_length = 50)
    
    def __str__(self):
        return f'{self.name} {self.surname}'


class Book(models.Model):
    id = models.PositiveIntegerField(auto_created = True, unique = True, primary_key = True)
    title = models.CharField(max_length = 100)
    author = models.ForeignKey(Author, on_delete = models.DO_NOTHING)
    description = models.TextField()
    genre = models.CharField(max_length = 50)
    pages = models.IntegerField()
    library = models.ForeignKey(Library, on_delete = models.DO_NOTHING)
    price = models.DecimalField(max_digits = 15, decimal_places = 2)
    quantity = models.PositiveIntegerField(default = 0)
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    
class Booking(models.Model):
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(unique = True)
    expires = models.DateTimeField()
    quantity = models.PositiveIntegerField(default = 1)
    status = models.CharField(max_length=10, choices=[
        ("Cancelled", "Cancelled"),
        ("Expired", "Expired"),
        ("Active", "Active"),
        ("Completed", "Completed")
    ])
    
    def __str__(self):
        return f'{self.user.first_name} - {self.book.title} (Quantity: {self.quantity}) ({self.status})'