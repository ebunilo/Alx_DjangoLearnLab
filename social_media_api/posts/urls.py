from rest_framework import routers

from .views import PostViewSet, CommentViewSet, FeedView
from django.urls import path
from django.urls import include

router = routers.DefaultRouter()

router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view({'get':'list'})),
    path('/posts/<int:pk>/like/', include('notifications.urls')),
    path('/posts/<int:pk>/unlike/', include('notifications.urls')),
]
