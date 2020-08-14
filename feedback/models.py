from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=100, blank=True)
    phone = models.IntegerField(blank=True)
    email = models.EmailField(max_length=100, blank=False)
    comments = models.TextField(blank=False)

    def __str__(self):
        return self.name

