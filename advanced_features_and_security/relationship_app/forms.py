from django.forms import ModelForm
from .models import Book


# Code added for loading form data on the Booking page
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

