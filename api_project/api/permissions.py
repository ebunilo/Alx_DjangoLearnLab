from rest_framework.permissions import BasePermission


class IsEmailVerified(BasePermission):
    """
    Custom permission to only allow access to users with verified emails.
    """
    def has_permission(self, request, view):
        # Assuming the user model has an 'is_email_verified' field.
        return request.user and request.user.is_authenticated and request.user.is_email_verified
