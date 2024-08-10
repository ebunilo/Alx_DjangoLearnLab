# Delete Book
### Delete the book and confirm the deletion by trying to retrieve all books again.
 
Book.objects.filter(title="Nineteen Eighty-Four").delete()
 
"""(1, {'bookshelf.Book': 1})"""

Book.objects.all()

"""<QuerySet []>"""