from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        extra_kwargs = {"key": {"required": False}}

    def create(self, validated_data):
        key = validated_data.get("key")
        if not key:
            raise serializers.ValidationError(
                {"key": "This field is required for POST requests."}
            )
        return super().create(validated_data)
