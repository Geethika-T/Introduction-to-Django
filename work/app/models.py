from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    is_employee = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)

class Book(models.Model):
    title=models.CharField(max_length=120)
    auhor=models.CharField(max_length=120)
    pdf=models.FileField(upload_to="book/pdf")
    cover=models.ImageField(upload_to="book/cover")
