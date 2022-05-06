from rest_framework.permissions import BasePermission


class AuthPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'get_me':
            return request.user.is_authenticated

        return True
