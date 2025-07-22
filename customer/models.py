from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=128)
    address = models.CharField(blank=True, null=True)

    def __str__(self):
        return self.customer_name