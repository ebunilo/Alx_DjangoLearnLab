from django.urls import path
from . import views

urlpatterns = [
    path('list_books/', views.list_books, name='list_books'),
    # path('list_view/<int:book_id>/', views.book_detail, name='book_detail'),  # Add URL for book detail page.
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Add URL for library detail page.
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('register/', views.UserRegisterView.as_view(), name='register'),  # Add URL for user registration.
]