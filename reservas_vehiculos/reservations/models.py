from django.db import models
from customers.models import Customers
from vehicles.models import Vehicles

# Create your models here.

class Booking(models.Model):
    reserve_status = [
        ('ACTIVE','Active'),
        ('EARRING','Earring'),
        ('CANCELED','Canceled'),
        ('FINISHED','Finished'),
    ]
    customer = models.ForeignKey(Customers, related_name='booking', on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicles, related_name='booking', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=reserve_status, default='EARRING')
    total_price = models.DecimalField(max_digits=20, decimal_places=2)

    