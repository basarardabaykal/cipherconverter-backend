from rest_framework import serializers
from serializers import BaseCipherSerializer
from models import Caesar

class CaesarSerializer(BaseCipherSerializer):
    class Meta:
        model = Caesar
    fields = [
        ""
    ]