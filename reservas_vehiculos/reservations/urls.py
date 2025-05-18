
from rest_framework.routers import DefaultRouter
from .viewsets import BookingViewSet

router = DefaultRouter()
router.register('reservations', BookingViewSet)

urlpatterns = [
    
] + router.urls