from rest_framework import serializers
from django.utils.timezone import datetime

from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        if value > datetime.now().year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
