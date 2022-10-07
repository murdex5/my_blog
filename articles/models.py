from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime
# Create your models here.


User = get_user_model()




class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    body = models.TextField()
    date = models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        return self.title
