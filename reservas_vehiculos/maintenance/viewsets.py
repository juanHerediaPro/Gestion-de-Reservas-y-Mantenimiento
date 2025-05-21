from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.exceptions import PermissionDenied

from .models import Maintenance, TypeOfMaintenance
from .serializers import MaintenanceSerializer, TypeOfMaintenanceSerializer
from .permissions import IsTechnical, IsEmployeeReservationAdvisor
from employees.models import Employee

class MaintenanceViewSet(viewsets.ModelViewSet):
    serializer_class = MaintenanceSerializer
    queryset = Maintenance.objects.all()

    def get_permissions(self):

        user = self.request.user 
        if not user.is_authenticated:
            return [IsAuthenticated()] 

        if IsTechnical().has_permission(self.request, self):
            return [IsAuthenticated(), IsTechnical()]
        
        elif  IsEmployeeReservationAdvisor().has_permission(self.request, self):
            if self.action in ['list']:
                return[IsAuthenticated(), IsEmployeeReservationAdvisor()]
            else:
                raise PermissionDenied("dont have permissions for this action")

        raise PermissionDenied("dont have permissions.")
    
    def perform_create(self, serializer):
        user = self.request.user
        try:
            employee = Employee.objects.get(user=user)
            serializer.save(employee=employee)
        except Employee.DoesNotExist:
            raise ValidationError("El usuario no está asociado a ningún empleado.")

class TypeOfMaintenanceViewSet(viewsets.ModelViewSet):
    serializer_class = TypeOfMaintenanceSerializer
    queryset = TypeOfMaintenance.objects.all()
    permission_classes = [IsAuthenticated, IsTechnical]