from rest_framework import generics, response, status, exceptions, request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsModerator, IsSeller, IsOwnerAndPending
from rest_framework.views import APIView
from .models import Advert
from accounts.models import Seller
from .serializers import (
    ListAdsSerializer,
    UpdateAdSerializer,
    AdCreateSerializer,
    AdUpdateDeleteSerializer,
    SellerAdsSerializer,
)
import pdb


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


class ListAdsView(generics.ListAPIView):
    queryset = Advert.objects.filter(status="A").order_by("-creation_date")
    serializer_class = ListAdsSerializer


class ListPendingAdsView(generics.ListAPIView):
    queryset = Advert.objects.all().filter(status="P")
    serializer_class = ListAdsSerializer
    permission_classes = [IsAuthenticated, IsModerator]


class ListRejectedAdsView(generics.ListAPIView):
    queryset = Advert.objects.all().filter(status="R")
    serializer_class = ListAdsSerializer
    permission_classes = [IsAuthenticated, IsModerator]


class ListExpiredAdsView(generics.ListAPIView):
    queryset = Advert.objects.all().filter(status="E")
    serializer_class = ListAdsSerializer
    permission_classes = [IsAuthenticated, IsModerator]


class StatusPartialUpdateView(generics.UpdateAPIView):
    queryset = Advert.objects.all()
    serializer_class = UpdateAdSerializer
    permission_classes = [IsAuthenticated, IsModerator]


class AdDetailDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdUpdateDeleteSerializer
    permission_classes = [IsAuthenticated, IsSeller, IsOwnerAndPending]


class CreateAdView(generics.CreateAPIView):
    serializer_class = AdCreateSerializer


class MyAdsView(generics.ListAPIView):
    serializer_class = ListAdsSerializer

    def get_queryset(self):
        user = Seller.objects.filter(user_id=self.request.user.id)[0]
        queryset = Advert.objects.all().filter(ad_owner_id=user.id)
        # import pdb; pdb.set_trace()
        return queryset

    permission_classes = [IsAuthenticated, IsSeller]


class AdDetailView(APIView):
    def get(self, request, pk):
        try:
            ad = Advert.objects.all().filter(pk=pk)[0]

            # pdb.set_trace()
            owner = ad.ad_owner.user.username
            ad.ad_views += 1

            return Response(
                {
                    "seller": owner,
                    "car_make": ad.car.make,
                    "car_model": ad.car.model,
                    "car_fuel": ad.car.fuel,
                    "ad_content": ad.ad_text,
                    "car_picture": ad.car.picture,
                    "car_price": ad.price,
                    "ad_date_created": ad.creation_date,
                    "seller_contact_number": ad.ad_owner.phone_number.national_number,
                    "ad_views": ad.ad_views,
                },
                ad.save(),
            )
        except:
            return Response(status=status.HTTP_403_FORBIDDEN)


class TopAdDetailView(APIView):
    def get(self, request):
        try:
            ad = Advert.objects.all().order_by("-ad_views")[0]

            # pdb.set_trace()
            owner = ad.ad_owner.user.username

            return Response(
                {
                    "seller": owner,
                    "car_make": ad.car.make,
                    "car_model": ad.car.model,
                    "car_fuel": ad.car.fuel,
                    "ad_content": ad.ad_text,
                    "car_picture": ad.car.picture,
                    "car_price": ad.price,
                    "ad_date_created": ad.creation_date,
                    "seller_contact_number": ad.ad_owner.phone_number.national_number,
                    "ad_views": ad.ad_views,
                }
            )
        except:
            return Response(status=status.HTTP_403_FORBIDDEN)


class BuildTriger(APIView):
    pass


class ListSellersAdsView(APIView):
    def get(self, request):
        sellers = Seller.objects.all()

        serializer = SellerAdsSerializer(sellers, many=True)
        # pdb.set_trace()
        return Response(serializer.data)

    permission_classes = [IsAuthenticated, IsModerator]
