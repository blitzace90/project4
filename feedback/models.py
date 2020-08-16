from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Comment(models.Model):
    name = models.CharField(max_length=100, blank=False)
    phone = models.IntegerField(blank=False)
    email = models.EmailField(max_length=100, blank=False)
    comments = models.TextField(blank=False)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    order = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    image = CloudinaryField()

    def __str__(self):
        return self.order
