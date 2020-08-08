from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Category(models.Model):
    category = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.category


class Furniture(models.Model):
    name = models.CharField(blank=False, max_length=255)
    model = models.CharField(blank=False, max_length=255)
    desc = models.TextField(blank=False)
    quantity = models.IntegerField(blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    color = models.CharField(blank=False, max_length=255)
    picture = CloudinaryField()

    def __str__(self):
        return self.name
