from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Car
from accounts.models import Seller


class ListCarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class CreateCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ("make", "model", "fuel", "car_type", "color", "picture")

    def create(self, validated_data):
        seller = Seller.objects.get(user__pk=self.context["request"].user.id)
        validated_data["owner"] = seller
        return super(CreateCarSerializer, self).create(validated_data)


class UpdateCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ("make", "model", "fuel", "car_type", "color", "picture")


