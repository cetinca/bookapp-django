from PIL import Image
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100, unique=True)
    image = models.ImageField(default="default_book.jpg", upload_to="book_pics/")

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        created_on = models.DateTimeField(default=timezone.now)
        image = Image.open(self.image.path)

        if image.height > 300 or image.width > 200:
            output_size = (200, 300)
            image.thumbnail(output_size)
            image.save(self.image.path)


class BookRead(models.Model):
    read_on = models.DateTimeField(default=timezone.now)
    read_by = models.ForeignKey(User, on_delete=models.CASCADE)
    read_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    content = models.TextField(default="")

    class Meta:
        unique_together = ("read_by", "read_book")

    def __str__(self):
        return f'{self.read_book} {self.read_by}'
