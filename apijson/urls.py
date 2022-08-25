from django.urls import path, include


from .views import   jsonData ,snippet_list #getUserData,jsonDataInputInDB, GenericAPIView,


urlpatterns = [
    path("r/", include("rest_framework.urls")),
    
    path("", jsonData),   
    # path("j/", GenericAPIView.as_view()),
    path("json/", snippet_list),
    # path("u/",getUserData)
]
