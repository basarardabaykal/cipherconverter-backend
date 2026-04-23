from rest_framework import serializers
from .base import BaseCipherSerializer
from ..models import OTP


class OTPSerializer(BaseCipherSerializer):
    class Meta:
        model = OTP
        fields = [
            "input_text",
            "key",
            "operation",
            "output_text",
            "created_at",
            "created_by",
        ]
        read_only_fields = ["output_text", "created_at", "created_by"]

    def validate(self, attrs):
        key = attrs.get("key")
        input_text = attrs.get("input_text")

        if len(key) != len(input_text):
            raise serializers.ValidationError(
                "Key and input text must have equal lenghts."
            )

        return super().validate(attrs)