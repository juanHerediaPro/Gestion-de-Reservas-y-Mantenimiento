from django.db import models
from reservations.models import Booking

# Create your models here.

class Invoice(models.Model):
    booking = models.OneToOneField(Booking, related_name='invoice', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_day = models.DateField()
    payment_status = [
        ('PENDING','Pending'),
        ('PAID','Paid')
    ]
    status = models.CharField(max_length=10, choices=payment_status, default='PENDING')
