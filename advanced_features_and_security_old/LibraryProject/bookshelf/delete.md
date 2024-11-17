# Delete Book
### Delete the book and confirm the deletion by trying to retrieve all books again.
 
python manage.py shell

from bookshelf.models import Book

book = Book.objects.get(title='Nineteen Eighty-Four')

book.delete()

""" (1, {'bookshelf.Book': 1}) """

Book.objects.all()

""" <QuerySet []> """
