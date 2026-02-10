from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    """
    User address model.
    """

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="addresses")
    receiver_name = models.CharField(max_length=255)
    province = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    ward = models.CharField(max_length=100)
    detail_address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    is_default = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
