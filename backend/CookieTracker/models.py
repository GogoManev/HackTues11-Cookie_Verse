from django.db import models
from django.conf import settings

# Create your models here.

class Post(models.Model):
    poster = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=128)
    text = models.CharField(max_length=3000000)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    poster = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=300000)

class Forum(models.Model):
    name = models.CharField(max_length=2048)