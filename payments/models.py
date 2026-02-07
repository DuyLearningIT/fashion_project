from django.db import models


class PaymentTransaction(models.Model):
    """
    Separate payment table allows:
    - multiple gateways
    - retry payment
    - auditing
    """

    PROVIDER_CHOICES = [
        ("vnpay", "VNPay"),
        ("momo", "MoMo"),
        ("stripe", "Stripe"),
    ]

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("success", "Success"),
        ("failed", "Failed"),
    ]

    order = models.OneToOneField(
        "orders.Order", on_delete=models.CASCADE, related_name="payment")

    provider = models.CharField(max_length=20, choices=PROVIDER_CHOICES)
    transaction_code = models.CharField(max_length=255)

    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="pending")

    paid_at = models.DateTimeField(null=True, blank=True)

    raw_response = models.JSONField(null=True, blank=True)
