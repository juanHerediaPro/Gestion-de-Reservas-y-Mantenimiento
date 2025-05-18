from rest_framework import viewsets
from rest_framework.decorators import action

from .models import Employee, Position
from .serializers import EmployeeSerializers, PositionSerializers
from .permissions import IsEmployeeReservationAdvisor
from rest_framework.permissions import IsAuthenticated

class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializers
    queryset = Employee.objects.all()
    permission_classes = [IsEmployeeReservationAdvisor, IsAuthenticated]

    def perform_destroy(self, instance):
            related_user = instance.user
            instance.delete()
            if related_user:
                related_user.delete()
            

class PositionViewSet(viewsets.ModelViewSet):
    serializer_class = PositionSerializers
    queryset = Position.objects.all()
    permission_classes = [IsEmployeeReservationAdvisor, IsAuthenticated]

