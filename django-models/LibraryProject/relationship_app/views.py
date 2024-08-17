from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

from .models import Book, Library

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'


# User Login View (built-in)
class UserLoginView(LoginView):
    template_name = 'login.html'

# User logout View (built-in)
class UserLogoutView(LogoutView):
    template_name = 'login.html'


class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')
