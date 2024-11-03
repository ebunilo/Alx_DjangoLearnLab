# Create Book
### Create a Book instance with the title “1984”, author “George Orwell”, and publication year 1949.

python manage.py shell

from bookshelf.models import Book

Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

""" <Book:  Title: 1984, Author: George Orwell, Publication Date: 1949> """
