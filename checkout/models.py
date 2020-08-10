from django.db import models
from furnitures.models import Furniture
from django.contrib.auth.models import User

# Create your models here.
class Purchase(models.Model):
    furniture_id = models.ForeignKey(Furniture, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Purchase made for {self.furniture_id} by user#{self.user_id} on {self.purchase_date}"