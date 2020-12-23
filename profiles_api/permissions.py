from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Permission to allow users to edit their own profiles"""

    def has_object_permission(self, request, view, obj):
        """Check if user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnFeedItem(permissions.BasePermission):
    """Permission to allow users to edit their own feed items"""

    def has_object_permission(self, request, view, obj):
        """Check if user is trying to edit their own feed item"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
