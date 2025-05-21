from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from .serializers import BookingSerializer
from .permissions import IsEmployeeReservationAdvisor, IsCustomer
from .models import Booking
from customers.models import Customers

class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()    

    def get_permissions(self):
        user = self.request.user

        if not user.is_authenticated:
            return [IsAuthenticated()] 

        if IsCustomer().has_permission(self.request, self) or IsEmployeeReservationAdvisor().has_permission(self.request, self):
            return [IsAuthenticated()]

        raise PermissionDenied("this user dont have permissions.")
    
    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'customer'):
            return Booking.objects.filter(customer=user.customer)
        return Booking.objects.all()

    def perform_create(self, serializer):
        if hasattr(self.request.user, 'customer'):
            customer = Customers.objects.get(user=self.request.user)
            booking = serializer.save(customer=customer)
        else:
            booking = serializer.save()
        
        if booking.vehicle:
            booking.vehicle.condition = 'RESERVED'
            booking.vehicle.save()


        



