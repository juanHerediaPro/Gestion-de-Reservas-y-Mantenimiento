from rest_framework import serializers
from datetime import datetime, date

from .models import Customers

class CustomersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = [
            'first_name',
            'last_name',
            'id_card',
            'date_of_birth',
            'contact_number',
            'email',
            'address',
            'password'
        ]

    def validate_date_of_birth(self, value):
        if value > datetime.now().date():
            raise serializers.ValidationError("date of birth can not be in the future")
        return value
    
    def validate_existing_customer(self, attrs):
        if self.instance is None:
            if Customers.objects.filter(id_card=attrs['id_card']).exists():
                raise serializers.ValidationError("id card already exist")
            elif Customers.objects.filter(email=attrs['email']).exists():
                raise serializers.ValidationError("email already exist")
            return super().validate(attrs)
    
    def create(self, validated_data):
        return super().create(validated_data)