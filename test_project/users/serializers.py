from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    text = serializers.CharField(max_length=5000)
    pub_date = serializers.DateTimeField()