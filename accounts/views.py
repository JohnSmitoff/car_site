from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

from .serializers import UserSerializer

# Create your views here.


class UserCreate(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class SellerCreate(generics.CreateAPIView):
    serializer_class = UserSerializer
