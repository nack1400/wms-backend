from rest_framework import serializers
from .models import Product
from categories.serializers import CategorySerializer


class ProductReadSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"


class ProductCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        extra_kwargs = {
            "name": {"required": False},
            "packer": {"required": False},
            "brand": {"required": False},
            "identification_code": {"required": False},
            "memo": {"required": False},
            "category": {"required": False},
        }
