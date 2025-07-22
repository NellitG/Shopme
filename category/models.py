from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)
    category_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.category_name