from django.db import models

# Create your models here.
class Article(models.Model):
    work = models.CharField(max_length=100) 
    content = models.TextField()
    is_completed = models.BooleanField(default = False)