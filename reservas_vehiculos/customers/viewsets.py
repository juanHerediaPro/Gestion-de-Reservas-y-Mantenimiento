from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import CustomersSerializers
from .models import Customers
from .permissions import IsCustomer, IsEmployeeReservationAdvisor

class CustomersViewSets(viewsets.ModelViewSet):
    serializer_class = CustomersSerializers
    queryset = Customers.objects.all()


    @action(detail=False, methods=['GET','PUT'], permission_classes=[IsAuthenticated and IsCustomer or IsEmployeeReservationAdvisor])
    def personal_data(self, request):
        if request.method == 'GET':
            try:    
                customer = request.user.customer
                serializer = self.get_serializer(customer)
                return Response(serializer.data)
            except Customers.DoesNotExist:
                return Response({'detail': 'the customer was not found'}, status=404)
        if request.method == 'PUT':
            customer = request.user.customer
            serializer = self.get_serializer(customer , data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)


    def list(self, request, *args, **kwargs):
        if IsEmployeeReservationAdvisor().has_permission(request, self):
            return super().list(request, *args, **kwargs)
        raise MethodNotAllowed("GET method not allowed")
    
    def create(self, request, *args, **kwargs):
        if IsEmployeeReservationAdvisor().has_permission(request, self)  :    
            return super().create(request, *args, **kwargs)
        elif not request.user.is_authenticated:
            return super().create(request, *args, **kwargs)
        raise MethodNotAllowed("POST method not allowed")
    
    def update(self, request, *args, **kwargs):
        if IsEmployeeReservationAdvisor().has_permission(request, self) or IsCustomer.has_permission(self, request):
            return super().update(request, *args, **kwargs)
        raise MethodNotAllowed("PUT method not allowed.")

    def destroy(self, request, *args, **kwargs):
        if IsEmployeeReservationAdvisor().has_permission(request, self):
            return super().destroy(request, *args, **kwargs)
        raise MethodNotAllowed("DELETE method not allowed.")

    def partial_update(self, request, *args, **kwargs):
        if IsEmployeeReservationAdvisor().has_permission(request, self) or IsCustomer.has_permission(self, request):
            return super().partial_update(request, *args, **kwargs)
        raise MethodNotAllowed("PATCH method not allowed.")
    
    def retrieve(self, request, *args, **kwargs):
        if IsEmployeeReservationAdvisor().has_permission(request, self):
            return super().retrieve(request, *args, **kwargs)
        raise MethodNotAllowed("GET method not allowed.")