# from django.contrib.auth import authenticate, get_user_model
# from django.contrib.auth.models import update_last_login
# from django.utils.translation import gettext_lazy as _
# from rest_framework import exceptions, serializers
# from rest_framework.exceptions import ValidationError

# from rest_framework_simplejwt.settings import api_settings
# from rest_framework_simplejwt.tokens import RefreshToken, SlidingToken, UntypedToken

# from users.models import EmailBackend

# if api_settings.BLACKLIST_AFTER_ROTATION:
#     from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken

# from rest_framework_simplejwt.authentication import AUTH_HEADER_TYPES
# from rest_framework.response import Response
# from rest_framework import status, generics
# from rest_framework_simplejwt.serializers import TokenRefreshSerializer
# from rest_framework_simplejwt.exceptions import InvalidToken, TokenError











# class TokenObtainSerializer(serializers.Serializer):
#     username_field = get_user_model().USERNAME_FIELD
#     email=username_field
#     # default_error_messages = {
#     #     'no_active_account': _('No active account found with the given credentials')
#     # }

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.fields[self.username_field] = serializers.EmailField()

#     def validate(self, attrs):
#         authenticate_kwargs = {
#             self.username_field: attrs[self.username_field],
#         }
#         authenticate_kwargs["email"]=authenticate_kwargs.pop("username")
#         try:
#             authenticate_kwargs['request'] = self.context['request']
#         except KeyError:
#             pass

#         self.user = authenticate(**authenticate_kwargs)

#         # if not api_settings.USER_AUTHENTICATION_RULE(self.user):
#             # raise exceptions.AuthenticationFailed(
#             #     self.error_messages['no_active_account'],
#             #     'no_active_account',
#             # )

#         return self.user

#     @classmethod
#     def get_token(cls, user):
#         raise NotImplementedError('Must implement `get_token` method for `TokenObtainSerializer` subclasses')


# class TokenObtainPairSerializer(TokenObtainSerializer):
#     @classmethod
#     def get_token(cls, user):
#         return RefreshToken.for_user(user)

#     def validate(self, attrs):
#         data = super().validate(attrs)

#         refresh = self.get_token(self.user)

#         data['refresh'] = str(refresh)
#         data['access'] = str(refresh.access_token)

#         if api_settings.UPDATE_LAST_LOGIN:
#             update_last_login(None, self.user)

#         return data

# from rest_framework_simplejwt.views import TokenViewBase


# class TokenObtainPairView(TokenViewBase):
#     serializer_class = TokenObtainPairSerializer


# token_obtain_pair = TokenObtainPairView.as_view()


# class TokenRefreshView(TokenViewBase):
#     serializer_class = TokenRefreshSerializer


# token_refresh = TokenRefreshView.as_view()


# class CustomLoginView(TokenObtainPairView):
#     pass


# class CustomTokenRefreshView(TokenRefreshView):
#     pass