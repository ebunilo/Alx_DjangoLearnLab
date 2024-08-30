from django.db import models

# Create your models here.


class Book(models.Model):
    """ A simple Book model"""
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

    def __str__(self) -> str:
        return str(self.title)
