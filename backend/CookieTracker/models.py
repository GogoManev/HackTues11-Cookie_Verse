from django.db import models
from django.conf import settings

# Create your models here.

class Post(models.Model):
    poster = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owned_guilds')
    title = models.CharField(max_length=128)
    text = models.CharField(max_length=3000000)
    
