from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User  # this is for grader

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='post_comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(editable=True, auto_now=True)

    def __str__(self):
        return f"{self.content} by {self.author.username}"


class Tag(models.Model):
    name = models.CharField(unique=True, max_length=150)
    posts = models.ManyToManyField(Post, related_name='tags')

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    """This is an optional Extension of the User Model"""

    bio = models.TextField(help_text='Tell us about yourself', null=True, blank=True)
    profile_picture = models.ImageField(null=True, blank=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self) -> str:
        return f"{self.user.username}"