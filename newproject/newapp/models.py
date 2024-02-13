from django.db import models

# Create your models here.
class product(models.Model):
    item_name =models.CharField(max_length=20)
    item_img =models.ImageField()