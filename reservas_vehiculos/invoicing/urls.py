from rest_framework.routers import DefaultRouter
from .viewsets import InvoiceViewSet

router = DefaultRouter()
router.register('invoice',InvoiceViewSet)

urlpatterns = [
    
] + router.urls