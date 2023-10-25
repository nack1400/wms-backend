from rest_framework import serializers
from .models import User


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            "password",
            "is_superuser",
            "is_staff",
            "groups",
            "user_permissions",
        ]
        read_only_fields = ["username"]


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            "is_superuser",
            "is_staff",
            "groups",
            "user_permissions",
        ]
