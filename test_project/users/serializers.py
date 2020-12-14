from django.conf import settings
from django.contrib.auth import authenticate
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'is_active', 'last_login', 'is_superuser')
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            return User.objects.create_user(**validated_data)
