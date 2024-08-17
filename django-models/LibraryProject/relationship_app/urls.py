from django.urls import path
from . import views

urlpatterns = [
    path('list_books/', views.list_books, name='list_books'),
    # path('list_view/<int:book_id>/', views.book_detail, name='book_detail'),  # Add URL for book detail page.
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Add URL for library detail page.
]