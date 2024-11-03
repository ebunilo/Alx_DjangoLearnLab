from django.db import models


class Book(models.Model):
    """
        A Django model to represent a book in the database.

        Attributes:
        -----------
        title : CharField
            The title of the book, with a maximum length of 200 characters.
        author : CharField
            The author of the book, with a maximum length of 100 characters.
        publication_year : IntegerField
            The year the book was published. This field is optional and can be left blank or null.
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        """
               Returns a string representation of the Book instance.

               Returns:
               --------
               str
                   A string in the format "Title: {title}, Author: {author}, Publication Date: {publication_year}".
        """
        return f" Title: {self.title}, Author: {self.author}, Publication Date: {self.publication_year}"
