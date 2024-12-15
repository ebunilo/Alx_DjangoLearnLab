from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include

from .views import CustomUserViewSet, ProfileViewSet, RegisterView, CustomLoginView

router = DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='user')
router.register(r'profiles', ProfileViewSet, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', obtain_auth_token),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('follow/<int:user_id>/', FollowUsers.as_view() ),
    path('unfollow/<int:user_id>/', UnFollowUsers.as_view()),
]

