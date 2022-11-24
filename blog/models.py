from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from book.models import Book


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100, default="title")
    content = models.TextField(default="content")
    read_on = models.DateTimeField(default=timezone.now)
    read_by = models.ForeignKey(User, on_delete=models.CASCADE)
    read_book = models.ForeignKey(Book, on_delete=models.CASCADE)
