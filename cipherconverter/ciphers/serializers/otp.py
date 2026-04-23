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