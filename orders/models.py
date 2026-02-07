from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    """
    Order model.
    """

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="orders")
    address = models.ForeignKey("address.Address", on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_fee = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    final_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default="pending")
    note = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.email}"


class OrderItem(models.Model):
    """
    Items in an order.
    """

    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE)
    product_variant = models.ForeignKey(
        "products.ProductVariant", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Item {self.id} of Order {self.order.id}"
