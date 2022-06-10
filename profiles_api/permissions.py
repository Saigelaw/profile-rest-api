from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profiel"""

    def has_object_permission(self, request, view, obj):
        """Check if user is trying ti update their own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id