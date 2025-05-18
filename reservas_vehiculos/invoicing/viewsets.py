from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import InvoiceSerializer
from .models import Invoice
from .permissions import IsEmployeeReservationAdvisor

class InvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()
    permission_classes = [IsAuthenticated,IsEmployeeReservationAdvisor]