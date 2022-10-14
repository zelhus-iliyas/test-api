from django.urls import path

from .google import get_google_login_signup_token
from .views import (
    CreateClient,
    DeleteClient,
    GetClient,
    GetClientList,
    UpdateClient,
)
from .calender import (
    GoogleCalendarInitView,
    GoogleCalendarRedirectView,
)

urlpatterns = [
    ###########crud##################
    path("create/", CreateClient.as_view()),
    path("get/", GetClientList.as_view()),
    path("get/<int:pk>/", GetClient.as_view()),
    path("update/<int:pk>/", UpdateClient.as_view()),
    path("delete/<int:pk>/", DeleteClient.as_view()),
    ###########calender##############
    path("calender/", GoogleCalendarInitView),
    ###########google-login##########
    path("token/google/", get_google_login_signup_token),
]
