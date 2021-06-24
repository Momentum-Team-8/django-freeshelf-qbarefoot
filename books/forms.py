from django.forms import ModelForm

from .models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'title', 
            'author',
            'book_URL',
            'description',
            'created_at',
        ]