from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.CharField(max_length=50)
    isbn = models.CharField(max_length=20)
    
    def __str__(self):
        return self.title
