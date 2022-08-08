from django.contrib import admin

from .models import Post, Image


class PostAdmin(admin.ModelAdmin):
    model = Post

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("title", "content", "is_published", "author"),
            },
        ),
    )

    fieldsets = ((None, {"fields": ("title", "content", "is_published", "author")}),)

    list_display = ("title", "author", "is_published", "created_at")
    list_filter = ("is_published",)

    search_fields = ("title", "content")
    ordering = ("-created_at",)


admin.site.register(Post)
admin.site.register(Image)
