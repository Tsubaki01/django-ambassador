from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# from .serializers import ProductSerializer, LinkSerializer, OrderSerializer
from common.authentication import JWTAuthentication
from common.serializers import UserSerializer
from core.models import User#, Product, Link, Order
# from django.core.cache import cache


class AmbassadorAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, _):
        ambassadors = User.objects.filter(is_ambassador=True)
        serializer = UserSerializer(ambassadors, many=True)
        return Response(serializer.data)