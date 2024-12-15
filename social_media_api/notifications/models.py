from django.db import models
from django.contrib.auth import get_user_model
from posts.models import Post
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class Notification(models.Model):
    recipient = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='notifications')
    actor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='actor_notifications')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    verb = models.CharField(max_length=50, unique=True)
    target = GenericForeignKey('content_type','post')
    timestamp = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.verb

    class Meta:
        indexes = [
            models.Index(fields=('content_type', 'post'))
        ]