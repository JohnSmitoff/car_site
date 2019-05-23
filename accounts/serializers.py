from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Seller


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ("phone_number", "gender")


class UserSerializer(serializers.ModelSerializer):
    seller = SellerSerializer(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'seller')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        seller_data = validated_data.pop("seller")
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        Seller.objects.create(user=user, **seller_data)

        return user
