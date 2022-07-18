from rest_framework import serializers

from core.models import Product, Link#, OrderItem, Order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class LinkSerializer(serializers.ModelSerializer):
    orders = serializers.SerializerMethodField('get_orders')

    # def get_orders(self, obj):
    #     return OrderSerializer(Order.objects.filter(code=obj.code), many=True).data

    class Meta:
        model = Link
        fields = '__all__'