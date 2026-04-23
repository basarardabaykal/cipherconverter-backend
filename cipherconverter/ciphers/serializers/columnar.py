from rest_framework import serializers
from .base import BaseCipherSerializer
from ..models import Columnar

class ColumnarSerializer(BaseCipherSerializer):
    class Meta:
        model = Columnar
        fields = [
            "input_text",
            "output_text",
            "created_at",
            "created_by",
            "operation",
            "key",
        ]
        read_only_fields = ["created_at", "created_by", "output_text"]

    def validate(self, attrs):
        key = attrs.get("key")

        if key < 2:
            raise serializers.ValidationError("Key cannot be smaller than 2.")
        
        if key > len(attrs.get("input_text")):
            raise serializers.ValidationError("Key cannot be larger than input size.")
            
        return super().validate(attrs)