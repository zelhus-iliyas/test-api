from django.urls import path, include


from .views import   jsonData ,snippet_list #getUserData,jsonDataInputInDB,


urlpatterns = [
    path("r/", include("rest_framework.urls")),
    
    path("", jsonData),   
    # path("j/", jsonDataInputInDB),
    path("json/", snippet_list),
    # path("u/",getUserData)
]
