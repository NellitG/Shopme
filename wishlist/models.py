from django.db import models

# Create your models here.
class Wishlist(models.Model):
    wishlist_id = models.AutoField(primary_key=True)

    def __str__(self):
        return f"Wishlist {self.wishlist_id}"