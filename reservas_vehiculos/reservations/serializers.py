from rest_framework import serializers
from .models import Booking
from datetime import datetime, date

from vehicles.serializers import VehiclesSerializers
from customers.serializers import CustomersSerializers
from vehicles.models import Vehicles

class BookingSerializer(serializers.ModelSerializer):

    vehicle_detail = VehiclesSerializers(source='vehicle',read_only=True)
    customers = CustomersSerializers(source='customer',read_only=True)
    
    class Meta:
        model = Booking
        fields = [
            'id',
            'customer',
            'vehicle',
            'start_date',
            'end_date',
            'status',
            'total_price',
            'vehicle_detail',
            'customers'
        ]
        read_only_fields = ['total_price']

    def validate_start_date_end_date(self, attrs):
        if attrs['start_date'] > datetime.now().date():
            raise serializers.ValidationError("start date can not be in the future")
        elif attrs['end_date'] > datetime.now().date():
            raise serializers.ValidationError("end date cat not be in the future")
        return super().validate(attrs)
    
    def validate(self, attrs):
        start = attrs.get('start_date')
        end = attrs.get('end_date')
        vehicle = attrs.get('vehicle')

        if start and end and vehicle:
            if start > end:
                raise serializers.ValidationError("Start date must be before end date")
            days = (end - start).days + 1
            price = vehicle.price_per_day * days
            attrs['total_price'] = price
        return attrs
    
    def validate_vehicle(self, value):
        if value.condition != 'AVAILABLE':
            raise serializers.ValidationError("this car is not available")
        return value

    
    
    