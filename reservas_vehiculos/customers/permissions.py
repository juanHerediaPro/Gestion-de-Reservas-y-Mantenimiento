from rest_framework import permissions

class IsCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="customer")
    
    
class IsEmployeeReservationAdvisor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Employee(Reservation Advisor)").exists()