from django.urls import include, path
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Shape Backend Challenge",
        default_version='v1',
        description="Builded by Emerson Guedes",
        contact=openapi.Contact(email="guedes.emerson@hotmail.com"),
        license=openapi.License(name="All Rights Reserved to: Emerson Guedes de Oliveira"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("v1/vessel/", include("vessel.urls", namespace='api-vessel')),
    path("v1/equipment/", include("equipment.urls", namespace='api-equipment')),
    path("admin/", admin.site.urls),
    path("", schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]