from django.db import models

# Create your models here.
class Order_item(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"OrderItem {self.order_item_id} - Quantity: {self.quantity}, Price: {self.price}"