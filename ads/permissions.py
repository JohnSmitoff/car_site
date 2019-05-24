from rest_framework.permissions import BasePermission, SAFE_METHODS
from accounts.models import Moderator, User


class IsModerator(BasePermission):
    def has_permission(self, request, view):
        #import pdb; pdb.set_trace()

        moderator = Moderator.objects.filter(user__pk=request.user.id).exists()

        if moderator or (request.user.is_superuser and not request.method == "POST"):
            return True

        return False
