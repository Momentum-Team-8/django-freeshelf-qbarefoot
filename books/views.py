from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Book


# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return redirect ("list_books")
    return render(request, "books/homepage.html")

@login_required
def list_books(request):
    books = Book.objects.all().order_by('created_date')
    return render(request, "books/list_books.html",
                  {"books": books})