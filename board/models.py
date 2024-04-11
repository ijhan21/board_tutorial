from django.db import models

# Create your models here.
class Content(models.Model):    
    content = models.TextField()
    title = models.CharField(max_length=200)

class Comment(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    comment = models.TextField()