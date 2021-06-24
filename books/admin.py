
from books.models import Category, User, Book
from django.contrib import admin

# Register your models here.
admin.site.register(User)
admin.site.register(Book)
admin.site.register(Category)