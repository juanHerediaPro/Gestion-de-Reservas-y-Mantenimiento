from rest_framework import viewsets
from .serializers import VehiclesSerializers, ColorSerializer, VehicleModelSerializer
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Vehicles, Color, VehicleModel
from .permissions import IsCustomer, IsEmployeeReservationAdvisor

class VehiclesViewSet(viewsets.ModelViewSet):
    serializer_class = VehiclesSerializers
    queryset = Vehicles.objects.all()
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['GET'], permission_classes=[IsCustomer | IsEmployeeReservationAdvisor])
    def check_availability(self, request):
        condition = Vehicles.objects.filter(condition='AVAILABLE')
        serializer = VehiclesSerializers(condition, many=True)
        return Response(serializer.data)
    
    def list(self, request, *args, **kwargs):
        if IsEmployeeReservationAdvisor().has_permission(request, self):
            return super().list(request, *args, **kwargs)
        raise MethodNotAllowed("GET method not allowed")
    
    def create(self, request, *args, **kwargs):
        if IsEmployeeReservationAdvisor().has_permission(request, self):    
            return super().create(request, *args, **kwargs)
        raise MethodNotAllowed("POST method not allowed")
    
    def update(self, request, *args, **kwargs):
        if IsEmployeeReservationAdvisor().has_permission(request, self):
            return super().update(request, *args, **kwargs)
        raise MethodNotAllowed("PUT method not allowed.")

    def destroy(self, request, *args, **kwargs):
        if IsEmployeeReservationAdvisor().has_permission(request, self):
            return super().destroy(request, *args, **kwargs)
        raise MethodNotAllowed("DELETE method not allowed.")

    def partial_update(self, request, *args, **kwargs):
        if IsEmployeeReservationAdvisor().has_permission(request, self):
            return super().partial_update(request, *args, **kwargs)
        raise MethodNotAllowed("PATCH method not allowed.")
    
    def retrieve(self, request, *args, **kwargs):
        if IsEmployeeReservationAdvisor().has_permission(request, self):
            return super().retrieve(request, *args, **kwargs)
        raise MethodNotAllowed("GET method not allowed.")
    
class ColorViewSet(viewsets.ModelViewSet):
    serializer_class = ColorSerializer
    queryset = Color.objects.all()
    permission_classes = [IsAuthenticated, IsEmployeeReservationAdvisor]

class VehicleModelViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleModelSerializer
    queryset = VehicleModel.objects.all()
    permission_classes = [IsAuthenticated, IsEmployeeReservationAdvisor]