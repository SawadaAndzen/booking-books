from django.contrib import admin
from .models import Library, Book, Booking, Author


admin.site.register(Library)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Booking)