from rest_framework import serializers
from datetime import datetime, date

from .models import Position, Employee

class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'first_name',
            'last_naem',
            'id_card',
            'date_of_birth',
            'contact_number',
            'email',
            'address',
            'password',
            'position'
        ]

    def validate_date_of_birth(self, value):
        if value > datetime.now().date():
            raise serializers.ValidationError("date of birth can not be in the future")
        return value
    
    def validate_existing_customer(self, attrs):
        if self.instance is None:
            if Employee.objects.filter(id_card=attrs['id_card']).exists():
                raise serializers.ValidationError("id card already exist")
            elif Employee.objects.filter(email=attrs['email']).exists():
                raise serializers.ValidationError("email already exist")
            return super().validate(attrs)
            

class PositionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'
