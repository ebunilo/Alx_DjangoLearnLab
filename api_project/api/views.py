from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets

from .models import Book
from .serializers import BookSerializer

# Create your views here.


class BookList(generics.ListAPIView):
    """Uses serializer to retrieve and return book data"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """Handles common CRUD operations on Book model"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser | IsAuthenticated]
