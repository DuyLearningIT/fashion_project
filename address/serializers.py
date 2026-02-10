from .models import Address
from rest_framework import serializers


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["id", "user", "receiver_name", "province", "district", "ward",
                  "detail_address", "phone", "is_default"]
        # read_only_fields = ["id", "user"] Donnot allow user to be set manually
