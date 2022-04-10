from django.contrib.auth import models as auth_models
from django.core.validators import MinLengthValidator
from django.db import models

from car_api.account import managers as custom_manager
from car_api.common_tools.SoftDeleteMixin import SoftDeleteMixin


class AuthUser(auth_models.AbstractUser, auth_models.PermissionsMixin, SoftDeleteMixin):

    USERNAME_MAX_LENGTH = 15
    FIRST_NAME_MAX_LENGTH = 15
    LAST_NAME_MAX_LENGTH = 15

    email = models.EmailField(
        null=True,
        blank=True,
    )
    date_joined = models.DateField(auto_now_add=True)
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(MinLengthValidator(1),)
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(MinLengthValidator(1),)
    )
    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
    )

    is_deleted = models.BooleanField(
        default=False
    )

    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    objects = custom_manager.AuthUserManager()
