from rest_framework.generics import ListAPIView
from django.shortcuts import render

from .models import Book
from .serializers import BookSerializer

# Create your views here.


class BookList(ListAPIView):
    """Uses serializer to retrieve and return book data"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
