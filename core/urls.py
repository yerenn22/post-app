from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions, routers

from apps.user.views import UserViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Yoko - Post App API",
        default_version="v1",
        description="Yoko - Post App API Description",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()

router.register(r"users", UserViewSet, basename="users")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0)),
    path("api-auth/", include("rest_framework.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
