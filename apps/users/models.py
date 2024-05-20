from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.shared.models import AbstractBaseModel
from apps.shop.models import Product


class User(AbstractUser, AbstractBaseModel):
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default-user-avatar.jpg', null=True)
    born = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
