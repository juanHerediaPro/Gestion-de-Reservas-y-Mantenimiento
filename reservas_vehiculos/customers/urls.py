from rest_framework.routers import DefaultRouter
from .viewsets import CustomersViewSets

router = DefaultRouter()
router.register('customers', CustomersViewSets)

urlpatterns = [
    
] + router.urls