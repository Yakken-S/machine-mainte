from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """拡張ユーザーモデル"""
    username = models.CharField("従業員番号", max_length=12, unique=True)

    class Meta:
        verbose_name_plural = "CustomUser"