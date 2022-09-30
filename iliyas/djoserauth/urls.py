from django.contrib import admin
from django.urls import path, include

from testt.views import CustomLoginView

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("token/", CustomLoginView.as_view(),name='login'),
    # path("token/refresh/", CustomTokenRefreshView.as_view(),name='login'),
    path("u/", include("djoser.urls")),
    path("u/", include("djoser.social.urls")),
]
