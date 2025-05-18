from django.db import models
from vehicles.models import Vehicles
from employees.models import Employee

# Create your models here.

class TypeOfMaintenance(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

class Maintenance(models.Model):
    vehicle = models.ForeignKey(Vehicles, related_name='maintenance', on_delete=models.CASCADE)
    employee = models.ManyToManyField(Employee, related_name='maintenance')
    type_of_maintenance = models.ManyToManyField(TypeOfMaintenance, related_name='Maintenance')
    date = models.DateField()
    cost = models.DecimalField(max_digits=10 , decimal_places=2)
    description = models.TextField(blank=True)
