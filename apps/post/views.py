from rest_framework import mixins
from rest_framework import viewsets

from .models import Post
from .serializers import PostSerializer


class PostViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permission_classes = ()
