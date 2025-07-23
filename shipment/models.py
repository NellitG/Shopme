from django.db import models

# Create your models here.
class Shipment(models.Model):
    shipment_id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')])
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"Shipment {self.shipment_id} - {self.shipment_status} to {self.city}, {self.country}"
