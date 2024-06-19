from rest_framework.permissions import BasePermission

class IsAuthenticatedOrCreateOnly(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create':
            return True
        return request.user and request.user.is_authenticated
