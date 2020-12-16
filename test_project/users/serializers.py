from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериалайзер для нашего юзера"""
    class Meta:
        model = User
        fields = "__all__"
