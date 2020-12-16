from rest_framework import permissions


class IsOwnerAndAdminOrReadOnly(permissions.BasePermission):
    """Разрешение на удаление и изменение профиля есть только у Администратора и Владельца"""
    def has_object_permission(self, request, view, obj):
        if request.method in ('DELETE', 'PUT', 'PATCH'):
            return obj == request.user or request.user.is_superuser
        return True
