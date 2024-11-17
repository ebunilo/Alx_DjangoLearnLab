python ../manage.py shell

from .models import Author, Book, Library, Librarian

# Query all books by a specific author
# Retrieve the author by name
author = Author.objects.get(name="author_name")
author_name = Author.objects.get(name="author_name")
Author.objects.get(name=author_name)
# Get all books by the author
Book.objects.filter(author=author)



# List all books in a library.
# Retrieve the library by name
library_name = Library.objects.get(name="library_name")
Library.objects.get(name=library_name)
# Get all books in the library
Book.objects.filter(library=library_name)
# Or
library_name.books.all()


# Retrieve the librarian for a library.
# Retrieve the library by name
library_name = Library.objects.get(name="library_name")
# Get the librarian associated with the library
librarian = Librarian.objects.get(library=library_name)
print(library_name)


# Add book to a library
# Retrieve the library and book
library = Library.objects.get(name="library_name")
Book.objects.get(title="book_title")
book = Book.objects.get(title="book_title")
# Add the book to the library
library.books.add(book)
library.save()


# Add a list of books to the library
# Retrieve the author and library by names
author = Book.objects.get(name="author_name")
library = Library.objects.get(name="library_name")
# Retrieve the books you want to add
book1 = Book(title="Macbeth", author=author)
book2 = Book(title="Brutus", author=author)
book3 = Book(title="Twilight", author=author)
# Add the list of books
library.objects.add(book1, book2, book3)
# This does not require save() because it activates the many-to-many relationship and creates the record.


# Create a book
# Retrieve the author by name
author = Author.objects.get(name="author_name")
# create the new book
Book.objects.create(title="book_title", author=author)
