from rest_framework.routers import DefaultRouter
from .viewsets import MaintenanceViewSet, TypeOfMaintenanceViewSet

router = DefaultRouter()
router.register('maintenance',MaintenanceViewSet)
router.register('typeofmaintenance',TypeOfMaintenanceViewSet)

urlpatterns = [
    
] + router.urls