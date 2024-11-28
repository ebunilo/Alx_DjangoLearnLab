from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create test users
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.admin = User.objects.create_superuser(username='adminuser', password='adminpassword')
        
        # Create test authors and books
        self.author = Author.objects.create(name='Test Author')
        self.book1 = Book.objects.create(title='Test Book 1', author=self.author, publication_year=2020)
        self.book2 = Book.objects.create(title='Test Book 2', author=self.author, publication_year=2021)
        
        self.book_list_url = reverse('book-list')  # Update with actual view names
        self.book_detail_url = reverse('book-detail', kwargs={'pk': self.book1.id})
        self.book_create_url = reverse('book-create')  # Update with actual view names
        self.book_update_url = reverse('book-update', kwargs={'pk': self.book1.id})
        self.book_delete_url = reverse('book-delete', kwargs={'pk': self.book1.id})

    def test_list_books_authenticated(self):
        """Ensure authenticated users can list books."""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.book_list_url)
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_list_books_unauthenticated(self):
        """Ensure unauthenticated users can list books."""
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_book(self):
        """Test retrieving a specific book."""
        response = self.client.get(self.book_detail_url)
        serializer = BookSerializer(self.book1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_book_authenticated(self):
        """Ensure authenticated users can create a book."""
        self.client.login(username='adminuser', password='adminpassword')
        data = {'title': 'New Book', 'author': self.author.id, 'publication_year': 2023}
        response = self.client.post(self.book_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        """Ensure unauthenticated users cannot create a book."""
        data = {'title': 'New Book', 'author': self.author.id, 'publication_year': 2023}
        response = self.client.post(self.book_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        """Ensure authenticated users can update a book."""
        self.client.login(username='adminuser', password='adminpassword')
        data = {'title': 'Updated Book', 'author': self.author.id, 'publication_year': 2023}
        response = self.client.put(self.book_update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book')

    def test_update_book_unauthenticated(self):
        """Ensure unauthenticated users cannot update a book."""
        data = {'title': 'Updated Book', 'author': self.author.id, 'publication_year': 2023}
        response = self.client.put(self.book_update_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_book_authenticated(self):
        """Ensure authenticated users can delete a book."""
        self.client.login(username='adminuser', password='adminpassword')
        response = self.client.delete(self.book_delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_delete_book_unauthenticated(self):
        """Ensure unauthenticated users cannot delete a book."""
        response = self.client.delete(self.book_delete_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class AuthorAPITestCase(APITestCase):

    def setUp(self):
        self.author = Author.objects.create(name='Test Author')
        self.author_list_url = reverse('author-list')  # Update with actual view name

    def test_list_authors(self):
        """Ensure anyone can list authors."""
        response = self.client.get(self.author_list_url)
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
