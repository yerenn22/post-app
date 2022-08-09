from rest_framework import mixins
from rest_framework import viewsets

from .models import Post
from .permissions import PostPermissions
from .serializers import PostCreateSerializer, PostUpdateSerializer


class PostViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    permission_classes = (PostPermissions,)

    def get_queryset(self):
        if self.request.user.is_staff:
            return Post.objects.all()

        return Post.objects.filter(is_published=True)

    def get_serializer_class(self):
        if self.action in ["create", "list"]:
            return PostCreateSerializer

        return PostUpdateSerializer
