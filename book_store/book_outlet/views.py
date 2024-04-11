from django.shortcuts import render
from .models import Book

# Create your views here.

def index(request):
    books = Book.objects.all()
    return render(request, "book_outlet/index.html", {
        "books": books
    })

def book_detail(request, id):
    book = Book.objects.get(pk=id)
    return render(request, "book_outlet/book_detail.html", {
        "title",
        "author",
        "rating",
        "is_bestseller" 
    })