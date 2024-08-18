from django.urls import path
from . import views
from .views import list_books, UserLoginView, UserLogoutView

urlpatterns = [
    path('list_books/', list_books, name='list_books'),
    # path('list_view/<int:book_id>/', views.book_detail, name='book_detail'),  # Add URL for book detail page.
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Add URL for library detail page.
    path('login/', UserLoginView.as_view, template_name='login'),
    path('logout/', UserLogoutView.as_view, template_name='logout'),
    path('register/', views.register, name='register'),  # Add URL for user registration.
    path('register/', views.UserRegisterView.as_view(), template_name='register'),  # Add URL for user registration.
    path('admin_view/', views.admin_view, name='admin_view'),
    path('librarian_view/', views.librarian_view, name='librarian_view'),
    path('member_view/', views.member_view, name='member_view'),  # Add URL for member view.
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),  # Add URL for book deletion.  # Add URL for book deletion.  # Add URL for book deletion.  # Add URL for book deletion.  #
]