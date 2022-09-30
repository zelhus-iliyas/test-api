from django.urls import path
from . import views

urlpatterns = [
  path('account/', views.RegisterUserView.as_view(), name='register'),
  path('success/', views.RegisterUserSuccessView.as_view(), name='register_success'),
  path('failed/', views.RegisterUserFailedView.as_view(), name='register_failed'),
  path('access_token/', views.UserAccessToken.as_view(), name='register_access_token'),
]
