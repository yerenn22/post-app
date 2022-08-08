from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, Moderator, Administrator


class CustomUserAdmin(UserAdmin):
    model = User

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "username", "role", "password1", "password2"),
            },
        ),
    )

    fieldsets = ((None, {"fields": ("email", "username", "role", "password")}),)

    list_display = (
        "email",
        "username",
        "role",
        "is_active",
        "is_staff",
        "is_superuser",
    )

    search_fields = ("username", "email")
    ordering = ("username",)


admin.site.register(Moderator, CustomUserAdmin)
admin.site.register(Administrator, CustomUserAdmin)

admin.site.unregister(Group)
