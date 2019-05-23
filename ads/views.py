from rest_framework import generics, response, status, exceptions

from .models import Advert
from accounts.models import Seller
from .serializers import (
    ListAdsSerializer,
    UpdateAdSerializer,
    AdCreateSerializer,
    EditAdSerializer,
)


class MethodSerializerView(object):
    """
    Utility class for get different serializer class by method.
    For example:
    method_serializer_classes = {
        ('GET', ): MyModelListViewSerializer,
        ('PUT', 'PATCH'): MyModelCreateUpdateSerializer
    }
    """

    method_serializer_classes = None

    def get_serializer_class(self):
        assert self.method_serializer_classes is not None, (
            "Expected view %s should contain method_serializer_classes "
            "to get right serializer class." % (self.__class__.__name__,)
        )
        for methods, serializer_cls in self.method_serializer_classes.items():
            if self.request.method in methods:
                return serializer_cls

        raise exceptions.MethodNotAllowed(self.request.method)


class ListAds(generics.ListAPIView):
    queryset = Advert.objects.all().filter(status="A")
    serializer_class = ListAdsSerializer


class ListPendingAds(generics.ListAPIView):
    queryset = Advert.objects.all().filter(status="P")
    serializer_class = ListAdsSerializer


class ListRejectedAds(generics.ListAPIView):
    queryset = Advert.objects.all().filter(status="R")
    serializer_class = ListAdsSerializer


class ListExpiredAds(generics.ListAPIView):
    queryset = Advert.objects.all().filter(status="E")
    serializer_class = ListAdsSerializer


class StatusPartialUpdateView(generics.UpdateAPIView):
    queryset = Advert.objects.all()
    serializer_class = UpdateAdSerializer


class CreateAd(generics.CreateAPIView):
    serializer_class = AdCreateSerializer


class MyAds(generics.ListAPIView):
    serializer_class = ListAdsSerializer

    def get_queryset(self):
        user = Seller.objects.filter(user_id=self.request.user.id)[0]
        queryset = Advert.objects.all().filter(ad_owner_id=user.id)
        # import pdb; pdb.set_trace()
        return queryset
