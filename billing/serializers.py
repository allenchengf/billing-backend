from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    customer_name = serializers.CharField(max_length=255, required=False, allow_blank=True)
    customer_id = serializers.CharField(max_length=255, required=True)
    am = serializers.CharField(max_length=128, allow_blank=True, required=False)
    description = serializers.CharField(allow_blank=True, required=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)