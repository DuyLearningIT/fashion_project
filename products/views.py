from rest_framework.viewsets import ModelViewSet
from .models import Category, Product, ProductImage, ProductVariant
from .serializers import CategorySerializer, ProductSerializer, ProductImageSerializer, ProductVariantSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductImageViewSet(ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

    def get_queryset(self):
        product_id = self.request.query_params.get("product_id")
        if product_id:
            return ProductImage.objects.filter(product__id=product_id)
        return ProductImage.objects.all()


class ProductVariantViewSet(ModelViewSet):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer

    def get_queryset(self):
        product_id = self.request.query_params.get("product_id")
        if product_id:
            return ProductVariant.objects.filter(product__id=product_id)

        return ProductVariant.objects.all()
