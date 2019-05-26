from rest_framework import serializers
from django.db import models
from .models import Advert
from accounts.models import Seller


class ListAdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advert
        fields = "__all__"


class ListSellerSerializer(serializers.ModelSerializer):
    model = Seller
    fields = "__all__"


class EditAdSerializer(serializers.ModelSerializer):
    model = Advert
    fields = ("ad_text", "status")


class AdCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advert
        fields = ("car", "ad_text", "price", "creation_date")

    def create(self, validated_data):

        seller = Seller.objects.get(user__pk=self.context["request"].user.id)
        validated_data["ad_owner"] = seller
        validated_data["status"] = "P"
        return super(AdCreateSerializer, self).create(validated_data)


class AdDetailSerializer(serializers.ModelSerializer):
    models = Advert
    fields = ("id", "ad_text", "price")


class AdUpdateDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advert
        fields = ("ad_text", "price")


class UpdateAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advert
        fields = ("status",)


class AdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advert
        fields = ("price", "ad_text")


class SellerAdsSerializer(serializers.ModelSerializer):
    adverts = AdsSerializer(many=True, read_only=True)

    # import pdb pdb.set_trace()

    class Meta:
        model = Seller
        fields = ("user", "phone_number", "adverts")
