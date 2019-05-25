from rest_framework import generics
from .models import Car
from accounts.models import Seller
from .permissions import IsSeller, IsCarOwner, IsModerator
from rest_framework.permissions import BasePermission, IsAuthenticated

from .serializers import CreateCarSerializer, ListCarsSerializer, UpdateCarSerializer


class CreateCar(generics.CreateAPIView):
    serializer_class = CreateCarSerializer


class ListMyCars(generics.ListAPIView):

    serializer_class = ListCarsSerializer

    def get_queryset(self):
        user = Seller.objects.filter(user_id=self.request.user.id)[0]
        queryset = Car.objects.all().filter(owner_id=user.id)
        # import pdb; pdb.set_trace()
        return queryset


class UpdateCar(generics.RetrieveUpdateAPIView):
    serializer_class = UpdateCarSerializer
    permission_classes = [IsSeller, IsCarOwner, IsAuthenticated]

    def get_queryset(self):
        user = Seller.objects.filter(user_id=self.request.user.id)[0]
        queryset = Car.objects.all().filter(owner_id=user.id)
        # import pdb; pdb.set_trace()
        return queryset
