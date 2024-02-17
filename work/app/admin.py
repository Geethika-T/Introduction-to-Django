from django.contrib import admin

from app.models import CustomUser

from app.models import Book

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Book)