from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Book, Category


# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return redirect ("list_books")
    return render(request, "books/homepage.html")

@login_required
def list_books(request):
    books = Book.objects.all().order_by('-created_at')
    
    return render(request, "books/list_books.html", 
                  {"books": books})

def categories_books(request, slug):
    category = get_object_or_404(Category, slug=slug)
    books = category.books.all()

    return render(request, "books/categories_books.html", {"category": category, "books": books})