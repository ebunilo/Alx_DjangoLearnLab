from django.contrib import admin

from .models import Book, Library, Librarian, Author

# Register your models here.
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)
admin.site.register(Author)
