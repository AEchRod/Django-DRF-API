from rest_framework import permissions


class IsManager(permissions.BasePermission):
    # This method checks if a user has permission to access a view.
    # request.user refers to the user object associated with the current request.
    # groups accesses the groups associated with the user
    # filter(name="Manager") filters the groups to find the one with the name Manager
    # exists() checks whether any groups match the filter condition
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Manager').exists()

    def has_object_permission(self, request, view, obj):
        # Check if the user is a manager and has permission to access the specific menu item (obj)
        return request.user.groups.filter(name='Manager').exists()

class IsDeliveryCrew(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Delivery crew').exists()


class IsCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Customer').exists()

"""
from rest_framework import permissions

class IsManager(permissions.BasePermission):
    
    #Custom permission to only allow managers to perform certain actions.
    
    def has_permission(self, request, view):
        # Check if the user belongs to the 'Manager' group
        return request.user.groups.filter(name='Manager').exists()

class IsDeliveryCrew(permissions.BasePermission):
    
    #Custom permission to only allow delivery crew to perform certain actions.
    
    def has_permission(self, request, view):
        # Check if the user belongs to the 'Delivery Crew' group
        return request.user.groups.filter(name='Delivery Crew').exists()


class IsCustomer(permissions.BasePermission):
    
    #Custom permission to only allow customers to perform certain actions.
    
    def has_permission(self, request, view):
        # Check if the user is not in the 'Manager' or 'Delivery Crew' groups
        return not (request.user.groups.filter(name='Manager').exists() or
                    request.user.groups.filter(name='Delivery Crew').exists())

class IsOwner(permissions.BasePermission):
    
    #Custom permission to only allow the owner of an object to perform certain actions.
    
    def has_object_permission(self, request, view, obj):
        # Check if the user is the owner of the object
        return obj.user == request.user"""
