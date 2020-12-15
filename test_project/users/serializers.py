from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериалайзер для нашего юзера"""
    class Meta:
        model = User
        fields = ('id', 'username',
                  'first_name', 'last_name',
                  'is_active', 'last_login',
                  'is_superuser'
                  )

        def create(self, validated_data):
            return User.objects.create_user(**validated_data)


