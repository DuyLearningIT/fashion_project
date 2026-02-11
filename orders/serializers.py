from rest_framework import serializers
from django.db import transaction

from .models import Order, OrderItem
from products.models import ProductVariant


# ================= READ SERIALIZERS =================

class OrderItemSerializer(serializers.ModelSerializer):
    """Used for returning order items in responses"""

    line_total = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = "__all__"

    def get_line_total(self, obj):
        return obj.price * obj.quantity


class OrderDetailSerializer(serializers.ModelSerializer):
    """Used for GET /orders/{id}/"""

    items = OrderItemSerializer(many=True, read_only=True)
    subtotal = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = "__all__"

    def get_subtotal(self, obj):
        return sum(item.price * item.quantity for item in obj.items.all())

    def get_total_price(self, obj):
        subtotal = self.get_subtotal(obj)
        discount = getattr(obj, "discount_amount", 0) or 0
        shipping = getattr(obj, "shipping_fee", 0) or 0
        return subtotal - discount + shipping


# ================= CREATE SERIALIZERS =================

class CreateOrderItemSerializer(serializers.Serializer):
    """Only the data frontend is allowed to send when creating an order"""

    product_variant = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)


class CreateOrderSerializer(serializers.ModelSerializer):
    """Used for POST /orders/ checkout flow"""

    items = CreateOrderItemSerializer(many=True, write_only=True)

    total_amount = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True)
    final_amount = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Order
        fields = "__all__"

    @transaction.atomic
    def create(self, validated_data):
        items_data = validated_data.pop("items")

        # Create order first with temporary amounts
        order = Order.objects.create(
            **validated_data,
            total_amount=0,
            final_amount=0,
        )

        subtotal = 0

        # Create OrderItems with price snapshot from ProductVariant
        for item in items_data:
            variant = ProductVariant.objects.select_related(
                "product").get(id=item["product_variant"])

            line_total = variant.price * item["quantity"]
            subtotal += line_total

            OrderItem.objects.create(
                order=order,
                product=variant.product,
                product_variant=variant,
                quantity=item["quantity"],
                price=variant.price,
            )

        # Calculate final totals
        discount = order.discount_amount or 0
        shipping = order.shipping_fee or 0

        order.total_amount = subtotal
        order.final_amount = subtotal - discount + shipping
        order.save()

        return order
