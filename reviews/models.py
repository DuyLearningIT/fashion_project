from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    """
    Product reviews with moderation support.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="reviews")

    rating = models.PositiveSmallIntegerField()  # 1 → 5 stars
    comment = models.TextField(blank=True)

    is_approved = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
