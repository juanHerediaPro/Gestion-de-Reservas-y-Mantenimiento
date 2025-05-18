from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from .models import Employee

@receiver(post_save, sender=Employee)
def create_user_for_employee(sender, instance, created, **kwargs):
    if created and not instance.user:
        user = User.objects.create_user(
            username=instance.email,
            email=instance.email,
            password=instance.password  
        )
        instance.user = user
        instance.save()

        group_name = instance.position.name
        try:
            customers_group = Group.objects.get(name=group_name)
            user.groups.add(customers_group)
        except Group.DoesNotExist:
            print("el grupo no existe")

        