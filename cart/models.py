from django.db import models

# Create your models here.
class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Cart {self.cart_id} with quantity {self.quantity}"