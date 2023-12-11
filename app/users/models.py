from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

from .manager import UserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(max_length=30, unique=True, verbose_name="Почта")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    @property
    def access_token(self) -> str:
        """
        Позволяет получить токен доступа из экземпляра модели User.
        :return: str
        """
        return str(RefreshToken.for_user(self).access_token)

    @property
    def refresh_token(self) -> str:
        """
        Позволяет получить рефереш токен из экземпляра модели User.
        :return: str
        """
        return str(RefreshToken.for_user(self))

    def __str__(self) -> str:
        """
        :returns:
            [str]: Отвечает за корректное отображение объекта.
        """

