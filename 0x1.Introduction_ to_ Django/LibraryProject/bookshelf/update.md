# Update Book
### Update the book title to "Nineteen Eighty-Four and save the changes"

python manage.py shell

book = Book.objects.get(title="1984", author="George Orwell")

book.title = 'Nineteen Eighty-Four'

book.save()

Book.objects.all()

""" <QuerySet [<Book:  Title: Nineteen Eighty-Four, Author: George Orwell, Publication Date: 1949>]> """
