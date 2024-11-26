from rest_framework import generics

from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer


class BookListView(generics.ListAPIView):
    """List all books"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

class BookDetailView(generics.RetrieveAPIView):
    """Retrieve a single book"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateView(generics.CreateAPIView):
    """Create a new book"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateView(generics.UpdateAPIView):
    """Update an existing book"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDeleteView(generics.DestroyAPIView):
    """Delete a book"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorListView(generics.ListAPIView):
    """List all authors"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorCreateView(generics.CreateAPIView):
    """Create a new author"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
