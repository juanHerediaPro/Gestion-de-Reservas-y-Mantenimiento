from django.db.models.signals import post_save
from django.dispatch import receiver

from invoicing.models import Invoice
from reservations.models import Booking

@receiver(post_save, sender=Booking)
def create_invoice_for_booking(sender, instance, created,**kwargs):
    if created:
        Invoice.objects.create(
            booking = instance,
            amount = instance.total_price,
            payment_day = instance.start_date,
            status = 'PENDING'
        )