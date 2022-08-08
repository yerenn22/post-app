from django.db import models


class Role(models.TextChoices):
    MODERATOR = "MODERATOR", "Moderator"
    ADMINISTRATOR = "ADMINISTRATOR", "Administrator"
