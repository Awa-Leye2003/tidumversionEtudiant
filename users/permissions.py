from rest_framework import permissions

class IsAdminUser(permissions.BasePermission):
    """Permet l'accès uniquement aux administrateurs."""
    
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'

class IsScannerUser(permissions.BasePermission):
    """Permet l'accès aux utilisateurs scanner pour l'édition des scans seulement."""
    
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['admin', 'scanner']
