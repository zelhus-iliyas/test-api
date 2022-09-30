from django.urls import path
from . import views

urlpatterns = [
    path("", views.UserOauth2TokenAPIView.as_view(), name="user-oauth2-tokens-list"),
    path("account/", views.RegisterUserView.as_view(), name="register"),
]
