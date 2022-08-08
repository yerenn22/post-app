from rest_framework.serializers import ModelSerializer

from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "username", "role", "password")
        read_only_fields = ("id",)

        extra_kwargs = {
            "password": {
                "write_only": True,
            }
        }
