from rest_framework import serializers
from .models import Category, Product, ProductImage, ProductVariant


class CategorySerializer(serializers.ModelSerializer):
    # children = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ["id", "name", "description", "parent"]

    # def get_children(self, obj):
    #     return CategorySerializer(obj.children.all(), many=True).data


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "description", "category",
                  "base_price", "rating", "status"]


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["id", "product", "image_url"]


class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ["id", "product", "size", "color", "stock_quantity", "price"]
