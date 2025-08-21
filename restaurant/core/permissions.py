from rest_framework import permissions

class IsAdminOrManager(permissions.BasePermission):
    """Allow menu editing only for Admin/Manager"""
    def has_permission(self, request, view):
        # GET allowed for all
        if request.method in permissions.SAFE_METHODS:
            return True
        # POST/PUT/DELETE restricted
        user = request.user
        return user.is_authenticated and user.role in ("ADMIN", "MANAGER")