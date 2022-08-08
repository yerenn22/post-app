from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import UserManager, ModeratorManager, AdministratorManager
from .roles import Role


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(max_length=32, unique=True)
    username = models.CharField(max_length=32, unique=True)

    role = models.CharField(
        max_length=32,
        choices=Role.choices,
        default=Role.MODERATOR,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("username",)

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"


class Moderator(User):
    base_role = Role.MODERATOR

    objects = ModeratorManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role

        super().save(*args, **kwargs)

    class Meta:
        proxy = True
        verbose_name = "Moderator"
        verbose_name_plural = "Moderators"


class Administrator(User):
    base_role = Role.ADMINISTRATOR

    objects = AdministratorManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role

        super().save(*args, **kwargs)

    class Meta:
        proxy = True
        verbose_name = "Administrator"
        verbose_name_plural = "Administrators"
