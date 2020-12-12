from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


#
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(db_index=True, max_length=150, unique=True)
    first_name = models.CharField(db_index=True, max_length=30, unique=True)
    second_name = models.CharField(db_index=True, max_length=150, unique=True)
    last_login = models.DateTimeField(null=True, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)
    objects = UserManager()

    def __str__(self):
        """
        Возвращает строковое представление этого `User`.
        Эта строка используется, когда в консоли выводится `User`.
        """
        return self.username
