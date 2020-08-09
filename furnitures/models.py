from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Tag(models.Model):
    title = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.title

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
    tags = models.ManyToManyField(Tag)
    height = models.IntegerField(blank=False)
    breath = models.IntegerField(blank=False)
    length = models.IntegerField(blank=False)
    cost = models.DecimalField(max_digits=10, decimal_places=3, blank=False)
    picture = CloudinaryField()

    def __str__(self):
        return self.name
