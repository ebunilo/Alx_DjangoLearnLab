# Retrieve Book
### Retrieve and display all attributes of the book created previously.

python manage.py shell

Book.objects.get(title="1984", author="George Orwell")

""" <Book:  Title: 1984, Author: George Orwell, Publication Date: 1949> """
