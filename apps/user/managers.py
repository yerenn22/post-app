from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, username, password, **extra_fields):

        if not email:
            raise ValueError("User must have an email address")
        if not username:
            raise ValueError("User must have a username")

        extra_fields.setdefault("is_staff", True)

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)

        user.set_password(password)

        user.save()

        return user

    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        extra_fields.setdefault("role", "ADMINISTRATOR")

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have staff status")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have superuser status")

        return self.create_user(email, username, password, **extra_fields)


class ModeratorManager(UserManager):
    def create_user(self, email, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)

        return super().create_user(email, username, password, **extra_fields)

    def get_queryset(self):
        return super().get_queryset().filter(role="MODERATOR")


class AdministratorManager(UserManager):
    def create_user(self, email, username, password, **extra_fields):
        extra_fields.setdefault("role", "ADMINISTRATOR")
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return super().create_user(email, username, password, **extra_fields)

    def get_queryset(self):
        return super().get_queryset().filter(role="ADMINISTRATOR")
