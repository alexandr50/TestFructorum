from django.contrib.auth.models import AbstractUser
from django.db import models

from .manager import UserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(max_length=30, unique=True, verbose_name="Почта")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

