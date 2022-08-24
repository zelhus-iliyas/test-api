from django.urls import path, include

from .views import exampleView, snippets_list

urlpatterns = [

    path("", snippets_list),
    path('test-data/',exampleView),


]
