from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.models import User

class CustomTokenRefreshSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()

    def validate(self, attrs):
        refresh = RefreshToken(attrs["refresh_token"])
        data = {"access_token": str(refresh.access_token)}

        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "last_login", "is_superuser", "first_name", "last_name", "is_staff", "date_joined", "email", "spouse_name", "date_of_birth", "groups")
