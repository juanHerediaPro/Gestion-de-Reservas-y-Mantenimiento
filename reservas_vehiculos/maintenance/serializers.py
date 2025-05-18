from rest_framework import serializers
from .models import Maintenance, TypeOfMaintenance
from employees.serializers import EmployeeSerializers



class MaintenanceSerializer(serializers.ModelSerializer):
    employees = EmployeeSerializers(source='employee',read_only=True, many=True)

    class Meta:
        model = Maintenance
        fields = '__all__'

    def validate_vehicle(self, value):
        if value.condition == 'RESERVED':
            raise serializers.ValidationError("This vehicle is reserved")
        return value
    
    
class TypeOfMaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfMaintenance
        fields = '__all__'

