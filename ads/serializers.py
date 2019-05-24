from rest_framework import serializers
from .models import Advert
from accounts.models import Seller


class ListAdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advert
        fields = "__all__"


class EditAdSerializer(serializers.ModelSerializer):
    model = Advert
    fields = ("ad_text", "status")


class AdCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advert
        fields = "__all__"

    def create(self, validated_data):

        seller = Seller.objects.get(user__pk=self.context["request"].user.id)
        validated_data["ad_owner"] = seller
        return super(AdCreateSerializer, self).create(validated_data)


class AdUpdateDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advert
        fields = ("ad_text",)


class UpdateAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advert
        fields = ("status",)
