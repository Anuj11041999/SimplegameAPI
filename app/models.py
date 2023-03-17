from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publishedDate = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    