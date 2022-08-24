import os
from django.contrib import admin
from django.urls import path, include

# for swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Json API",
        default_version='v1',
        description="Breakdown of all APIs in this site as Docs. ",
        contact=openapi.Contact(email="a@a.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path(os.getenv("ADMIN_PAGE_URL") + "/", admin.site.urls),
    path("", include("apijson.urls")),
    
    path('new/', include("new.urls")),
    path(
        "swagger<format>.json.yaml",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redocs/", schema_view.with_ui("redoc",
         cache_timeout=0), name="schema-redoc"),
]
