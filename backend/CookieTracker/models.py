from django.db import models
from django.conf import settings

# Create your models here.

class Forum(models.Model):
    name = models.CharField(max_length=2048)

class Post(models.Model):
    poster = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=128)
    text = models.CharField(max_length=3000000)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    poster = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=300000)