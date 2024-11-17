from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f" Title: {self.title}, Author: {self.author}, Publication Date: {self.publication_year}"
    
    class Meta:
        permissions = [
            ('can_view', 'Can View'),
            ('can_create', 'Can Create'),
            ('can_edit', 'Can Edit'),
            ('can_delete', 'Can Delete'),
        ]


# Custom user manager
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, date_of_birth, password):
        if not email:
            raise ValueError("Email must be set")
        if not password:
            raise ValueError("password is required")
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, date_of_birth=date_of_birth)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
        
    def create_superuser(self, username, email, date_of_birth, password):
        user = self.create_user(username, email, date_of_birth, password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        
        return user

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)
    profile_photo = models.ImageField(blank=True)
    
    objects = CustomUserManager
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
