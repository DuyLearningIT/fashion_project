from rest_framework.viewsets import ModelViewSet
from .models import Review
from .serializers import ReviewSerializer


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        product_id = self.request.query_params.get("product_id")
        if product_id:
            return Review.objects.filter(product__id=product_id)
        return Review.objects.all()
