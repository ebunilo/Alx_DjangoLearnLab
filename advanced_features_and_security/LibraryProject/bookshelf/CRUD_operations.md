# CRUD Operations in Bookshelf App

### Create a Book instance with the title “1984”, author “George Orwell”, and publication year 1949.

from bookshelf.models import Book

new_book = Book(title="1984", author="George Orwell", publication_year=1949)

new_book.save()

"""There was no output for each of the commands which imply that the commands were successful"""


### Retrieve and display all attributes of the book created above.

Book.objects.filter(title="1984", author="George Orwell")

"""<QuerySet [<Book:  Title: 1984, Author: George Orwell, Publication Date: 1949>]>"""


### Update the book title to "Nineteen Eighty-Four and save the changes"

new_book.title = 'Nineteen Eighty-Four'

new_book.save()

Book.objects.all()

"""<QuerySet [<Book:  Title: Nineteen Eighty-Four, Author: George Orwell, Publication Date: 1949>]>"""


### Delete the book and confirm the deletion by trying to retrieve all books again.

Book.objects.filter(title="Nineteen Eighty-Four").delete()
 
"""(1, {'bookshelf.Book': 1})"""

Book.objects.all()

"""<QuerySet []>"""