from uuid import uuid4

from django.db import models

from apps.user.models import User


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=32)
    content = models.TextField()
    is_published = models.BooleanField(default=False)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "posts"
        verbose_name = "Post"
        verbose_name_plural = "Posts"


class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    image = models.ImageField(upload_to="posts/")

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="images",
    )

    def __str__(self):
        return self.post.title

    class Meta:
        db_table = "images"
        verbose_name = "Image"
        verbose_name_plural = "Images"
