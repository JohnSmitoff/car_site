from rest_framework.permissions import BasePermission, SAFE_METHODS
from accounts.models import Moderator, Seller


class IsModerator(BasePermission):
    def has_permission(self, request, view):
        # import pdb; pdb.set_trace()

        moderator = Moderator.objects.filter(user__pk=request.user.id).exists()

        if moderator or (request.user.is_superuser and not request.method == "POST"):
            return True

        return False


class IsSeller(BasePermission):
    def has_permission(self, request, view):
        # import pdb; pdb.set_trace()

        seller = Seller.objects.filter(user__pk=request.user.id).exists()

        if seller or request.user.is_superuser:
            return True

        return False


class IsCarOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        #import pdb; pdb.set_trace()
        try:
            seller = Seller.objects.all().filter(user__pk=request.user.id)[0]
            return (obj.owner.id == seller.id ) or request.user.is_superuser
        except:
            return False
