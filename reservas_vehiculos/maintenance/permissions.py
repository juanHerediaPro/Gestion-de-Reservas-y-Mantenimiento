from rest_framework import permissions

class IsTechnical(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Technical").exists()
    
class IsEmployeeReservationAdvisor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Employee(Reservation Advisor)").exists()