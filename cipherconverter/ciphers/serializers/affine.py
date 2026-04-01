from rest_framework import serializers
from .base import BaseCipherSerializer
from ..models import Affine

class AffineSerializer(BaseCipherSerializer):
    class Meta:
        model = Affine
        fields = [
            "input_text",
            "a",
            "b",
            "operation",
            "output_text",
            "created_at",
            "created_by"
        ]
        read_only_fields = ["output_text", "created_at", "created_by"]