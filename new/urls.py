from django.urls import path, include

from .views import snippets_list

urlpatterns = [

    path("", snippets_list),


]
