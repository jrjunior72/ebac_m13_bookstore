#product_serializer.py
from rest_framework import serializers 

from product.models.product import Category, Product
from product.serializers.category_serializer import CategorySerializer

class ProductSerializer(serializers.ModelSerializer): 
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())  # ← aqui!
    category = CategorySerializer(read_only=True, many=True) 
    categories_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True, many=True)

    class Meta: 
        model = Product 
        fields = ['title', 'description', 'price', 'active', 'category', 'categories_id', 'user']

    def create(self, validated_data):
        category_data = validated_data.pop('categories_id')
        user_data = validated_data.pop('user')

        product = Product.objects.create(**validated_data)
        for category in category_data:
            product.category.add(category)

        return product