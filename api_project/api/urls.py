from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include

from .views import BookList, BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),

    # Route for BookViewSet for all routes registered with router
    path('', include(router.urls)),
    
    # Obtain token using the obtain_auth_token view of DRF
    path('auth/', obtain_auth_token, name='auth_token')
]