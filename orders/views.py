from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Order
from .serializers import OrderDetailSerializer, CreateOrderSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).prefetch_related("items")

    def get_serializer_class(self):
        if self.action == "create":
            return CreateOrderSerializer
        return OrderDetailSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
