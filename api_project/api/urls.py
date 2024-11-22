from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import BookList, BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),

    # Route for BookViewSet for all routes registered with router
    path('', include(router.urls))
]