from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from .models import Customers

@receiver(post_save, sender=Customers)
def create_user_for_customers(sender, instance, created, **kwargs):
    if created and not instance.user:
        user = User.objects.create_user(
            username=instance.email,
            email=instance.email,
            password=instance.password  
        )
        instance.user = user
        instance.save()

        customers_group = Group.objects.get(name='customer')
        user.groups.add(customers_group)

        