# Retrieve Book
### Retrieve and display all attributes of the book created previously.
 
Book.objects.filter(title="1984", author="George Orwell")

"""<QuerySet [<Book:  Title: 1984, Author: George Orwell, Publication Date: 1949>]>"""
