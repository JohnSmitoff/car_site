from rest_framework import generics, response, status, exceptions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from .models import Car
from accounts.models import Seller
from django.contrib.auth.models import User
from .serializers import CreateCarSerializer, ListCarsSerializer
from ads.enums import AdStatusEnum
from django.shortcuts import get_object_or_404


class CreateCar(generics.CreateAPIView):
    serializer_class = CreateCarSerializer


class ListMyCars(generics.ListAPIView):

    serializer_class = ListCarsSerializer

    def get_queryset(self):
        user = Seller.objects.filter(user_id=self.request.user.id)[0]
        queryset = Car.objects.all().filter(owner_id=user.id)
        #import pdb; pdb.set_trace()
        return queryset
