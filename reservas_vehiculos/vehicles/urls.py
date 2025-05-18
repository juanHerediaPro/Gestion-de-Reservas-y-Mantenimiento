from django.urls import path
from rest_framework.routers import DefaultRouter
from .viewsets import VehiclesViewSet, ColorViewSet, VehicleModelViewSet

router = DefaultRouter()
router.register('vehicles', VehiclesViewSet)
router.register('color', ColorViewSet)
router.register('vehiculemodel', VehicleModelViewSet)


urlpatterns = [
    
] + router.urls