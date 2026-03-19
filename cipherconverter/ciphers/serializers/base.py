from rest_framework import serializers

class BaseCipherSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["created_by"] = user
        return super().create(validated_data)