from django.contrib.auth.models import User
from rest_framework import serializers
from typing import Dict


class UserSerializer(serializers.ModelSerializer):
    """Serializer class to validate User instances."""

    password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )

    class Meta:
        model = User
        fields = ("username", "password", "email", "first_name", "last_name")

    def create(self, validated_data: Dict[str, str]) -> User:
        """Create method for valid user data.

        Args:
            validated_data (Dict[str, str]): valid user data

        Returns:
            User: valid user
        """
        user = User.objects.create_user(**validated_data)
        return user
