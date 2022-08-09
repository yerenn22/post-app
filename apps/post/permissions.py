from rest_framework import permissions


class PostPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if (
            request.user.is_staff
            and request.method in ["PUT", "PATCH"]
            and request.user != obj.author
        ):
            return True

        if request.method == "DELETE" and request.user.is_superuser:
            return True

        return False
