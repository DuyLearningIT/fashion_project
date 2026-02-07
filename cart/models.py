from django.db import models
from django.contrib.auth.models import User


class Cart(models.Model):
    """
    Shopping cart model.
    """

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="carts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CartItem(models.Model):
    """
    Items in the shopping cart.
    """

    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="items")
    product_variant = models.ForeignKey(
        "products.ProductVariant", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
