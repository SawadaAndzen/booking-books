from django.db import models
from django.contrib.auth.models import User


class Library(models.Model):
    id = models.PositiveIntegerField(auto_created = True, unique = True)
    name = models.CharField(max_length = 50)
    desciption = models.TextField()
    adress = models.CharField(max_length = 150)
    work_time = models.TimeField()
    
    def __str__(self):
        return f"{self.name} - ({self.work_time})"
    
    
class Author(models.Model):
    name = models.CharField(max_length = 50)
    surname = models.CharField(max_length = 50)
    
    def __str__(self):
        return f'{self.name} {self.surname}'
    
    
'''   
class User(User):
    name = models.CharField(max_length = 50)
    surname = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    email = models.EmailField()
    phone = models.CharField(max_length = 100)
'''


class Book(models.Model):
    id = models.PositiveIntegerField(auto_created = True, unique = True)
    title = models.CharField(max_length = 100)
    author = models.ForeignKey(Author, on_delete = models.DO_NOTHING)
    description = models.TextField()
    genre = models.CharField(max_length = 50)
    pages = models.IntegerField()
    library = models.ForeignKey(Library, on_delete = models.DO_NOTHING)
    price = models.DecimalField(max_digits = 2)
    quantity = models.IntegerField()
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    
class Booking(models.Model):
      id_book = models.ForeignKey(Book, on_delete = models.DO_NOTHING)
      id_user = models.ForeignKey(User, on_delete = models.DO_NOTHING)
      date = models.DateTimeField()
      expires = models.DateTimeField()
      status = models.CharField(max_length=10, choices=[("Cancelled","Cancelled"), ("Expired", "Expired"), ("Active", "Active")])
      
      def __str__(self):
          return f'{self.date} - {self.expires} ({self.status})'