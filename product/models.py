from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_stock = models.IntegerField(default=0)
    product_image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.product_name