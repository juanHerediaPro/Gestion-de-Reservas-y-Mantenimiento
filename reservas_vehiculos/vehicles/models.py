from django.db import models

# Create your models here.

class VehicleModel(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)

class Color(models.Model):
    name = models.CharField(max_length=30, unique=True)

class Vehicles(models.Model):
    vehicle_type = [
        ('CAR','automobile'),
        ('VAN','van'),
        ('MOTORBIKE','Motorbike'),
        ('BUS','bus')
    ]
    vehicle_condition = [
        ('AVAILABLE','Available'),
        ('RESERVED','Reserved'),
        ('MAINTENANCE','In maintenance'),
        ('OUT_OF_SERVICE','Out of service')
    ]

    model = models.ForeignKey(VehicleModel, related_name='vehicles', on_delete=models.CASCADE)
    year = models.IntegerField()
    license_plate = models.CharField(max_length=10, unique=True)
    type = models.CharField(max_length=10, choices=vehicle_type)
    color = models.ForeignKey(Color, related_name='vehicles', on_delete=models.CASCADE)
    condition = models.CharField(max_length=20, choices=vehicle_condition, default='AVAILABLE')
    mileage = models.PositiveIntegerField()
    price_per_day = models.DecimalField(max_digits=10 , decimal_places=2)
