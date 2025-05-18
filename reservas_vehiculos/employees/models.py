from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Position(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee', null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_naem = models.CharField(max_length=100)
    id_card = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField()
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField()
    password = models.CharField(max_length=128, blank=False, null=True)
    position = models.ForeignKey(Position, related_name='employee', on_delete=models.CASCADE)