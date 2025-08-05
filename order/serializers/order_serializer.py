from rest_framework import serializers 

from order.models import Order 
from product.serializers.product_serializer import ProductSerializer

class OrderSerializer(serializers.ModelSerializer): 
    total = serializers.SerializerMethodField() 
    product = ProductSerializer(required=True, many=True)

    class Meta: 
        model = Order 
        fields = ['product', 'total'] 

    def get_total(self, instance):
        total = sum(product.price for product in instance.product.all()) 
        return total