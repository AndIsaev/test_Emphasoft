from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .permissions import IsOwnerAndAdminOrReadOnly
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """Вью для нашего юзера"""
    queryset = User.objects.all()
    authentication_classes = (TokenAuthentication, )
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwnerAndAdminOrReadOnly]
