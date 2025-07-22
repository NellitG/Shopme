from django.db import models

# Create your models here.
class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2) 
    payment_method = models.CharField(max_length=50, choices=[('credit_card', 'Credit Card'), ('Mpesa', 'Mpesa'), ('bank_transfer', 'Bank Transfer'), ('cash', 'Cash')]),
    

    def __str__(self):
        return f"Payment {self.payment_id} - Amount: {self.amount}, Method: {self.payment_method}"