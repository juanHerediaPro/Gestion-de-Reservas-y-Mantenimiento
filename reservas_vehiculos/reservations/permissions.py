from rest_framework import permissions

class IsCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="customer")
    
    def has_object_permission(self, request, view, obj):
        return obj.customer.user == request.user
   
    
class IsEmployeeReservationAdvisor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Employee(Reservation Advisor)").exists()