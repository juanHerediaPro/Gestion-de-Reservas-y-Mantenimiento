from rest_framework.routers import DefaultRouter
from .viewsets import EmployeeViewSet, PositionViewSet

router = DefaultRouter()
router.register('employees', EmployeeViewSet)
router.register('positions', PositionViewSet)

urlpatterns = [
    
] + router.urls