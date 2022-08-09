from rest_framework import serializers

from django.contrib.auth.models import AnonymousUser

from .models import Post, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("id", "image")
        ordering = ("id",)


class PostCreateSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    uploaded_images = serializers.ListField(
        child=serializers.FileField(
            max_length=128, allow_empty_file=False, use_url=False
        ),
        write_only=True,
    )

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "content",
            "images",
            "uploaded_images",
            "is_published",
            "author",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "is_published", "author", "created_at", "updated_at")
        ordering = ("-created_at",)

    def create(self, validated_data):
        images = validated_data.pop("uploaded_images")

        if self.context["request"].user != AnonymousUser():
            validated_data["author"] = self.context["request"].user

        post = Post.objects.create(**validated_data)

        for image in images:
            Image.objects.create(post=post, image=image)

        return post

    def validate(self, data):
        if len(data["uploaded_images"]) != 5:
            raise serializers.ValidationError("The number of photos must be five")

        return data


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "content",
            "images",
            "is_published",
            "author",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "images", "author", "created_at", "updated_at")
        ordering = ("-created_at",)
