from rest_framework import serializers
from serializers import BaseCipherSerializer
from models import Caesar

class CaesarSerializer(BaseCipherSerializer):
    class Meta:
        model = Caesar
    fields = [
        "input_text",
        "key",
        "operation",
        "output_text",
        "created_at",
        "created_by",
    ]
    read_only_fields = ["output_text, created_at, created_by"]