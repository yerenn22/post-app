from rest_framework import mixins
from rest_framework import viewsets

from .models import User
from .permissions import UserPermissions
from .serializers import UserSerializer


class UserViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = (UserPermissions,)
