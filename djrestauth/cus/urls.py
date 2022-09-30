from django.contrib import admin
from django.urls import path, include

from res.urls import GoogleLogin
from .views import *
urlpatterns = [
    path("t/", GetClient.as_view()),
]