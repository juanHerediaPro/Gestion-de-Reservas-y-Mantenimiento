from rest_framework import serializers
from .models import VehicleModel, Color, Vehicles
from datetime import datetime, date

class VehiclesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vehicles
        fields = [
            'id',
            'model',
            'year',
            'license_plate',
            'type',
            'color',
            'condition',
            'mileage',
            'price_per_day'
        ]

    def validate(self, attrs):
        current_year = datetime.now().year
        if attrs['year'] > current_year:
            raise serializers.ValidationError("date of model year cannot be in the future")
        return super().validate(attrs)

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

class VehicleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = '__all__'