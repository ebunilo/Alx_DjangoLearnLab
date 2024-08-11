# Create Book
### Create a Book instance with the title “1984”, author “George Orwell”, and publication year 1949.

from bookshelf.models import Book

new_book = Book(title="1984", author="George Orwell", publication_year=1949)

new_book.save()

"""There was no output for each of the commands which imply that the commands were successful"""
