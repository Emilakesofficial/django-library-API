from django.shortcuts import render

from django.views.generic import ListView 
from .models import Book

class BookViewList(ListView):
    model = Book
    template = 'book_list.html'
