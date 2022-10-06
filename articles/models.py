from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Articles(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    body = models.TextField()
    
    def __str__(self):
        return self.title