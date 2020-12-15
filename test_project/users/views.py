from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import UserSerializer



class UserViewSet(viewsets.ModelViewSet):
    """Вью для нашего юзера"""
    queryset = User.objects.all()
    authentication_classes = (TokenAuthentication, )
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)
