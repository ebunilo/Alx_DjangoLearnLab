from rest_framework.response import Response
from rest_framework.decorators import action

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    """Custom User Manager"""
    def create_user(self, email, password):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        
        return user

    def create_superuser(self, email, password):
        """Create a superuser with given email and password"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class CustomUser(AbstractUser):
    """Custom user"""
    email = models.EmailField(unique=True, max_length=255)
    username = models.CharField(unique=False, max_length=20)
    following = models.ManyToManyField("self", symmetrical=False, related_name="followers")
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    @action(detail=True, methods=['post'])
    def follow_user(self, request, pk=None):
        user_to_follow = self.get_object()
        request.user.following.add(user_to_follow)
        return Response({"status": "following"})

    @action(detail=True, methods=['post'])
    def unfollow_user(self, request, pk=None):
        user_to_unfollow = self.get_object()
        request.user.following.remove(user_to_unfollow)
        return Response({"status": "unfollowed"})


class Profile(models.Model):
    """User profile that ties to User"""
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    
    def __str__(self):
        return self.user.username