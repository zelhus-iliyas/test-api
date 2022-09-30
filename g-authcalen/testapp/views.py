from .models import *
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# # from rest_framework_simplejwt.tokens import Token
# from rest_framework.authtoken.models import Token
# from users.models import EmailBackend
# import jwt
# from newauth.settings import SECRET_KEY


# class AuthCustomTokenSerializer(serializers.Serializer):
#     email = serializers.EmailField()

#     def validate(self, attrs):
#         email = attrs.get("email")
#         if email:
#             user = EmailBackend.authenticate(email=email)
#             print("this is user", user)
#             if not user:
#                 msg = "Unable to log in with provided credentials."
#                 raise serializers.ValidationError(msg, code="authorization")
#         else:
#             msg = 'Must include "username" and "password".'
#             raise serializers.ValidationError(msg, code="authorization")

#         attrs["user"] = user
#         return attrs


# from rest_framework.response import Response
# from rest_framework.views import APIView

# # payload={"user":user}
# # token= jwt.encode(payload, SECRET_KEY).decode('utf-8')
# # print(token)
# class GoogleLoginView(APIView):
#     def post(self, request):
#         serializer = AuthCustomTokenSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             # serializer.save()
#             user = serializer.validated_data["user"]
#             # email = serializer.validated_data.email
#             token = Token.objects.create(user=user)
#             # print(token[0])
#             # payload={"user_id":user,"email":email}
#             # token= jwt.encode(payload, SECRET_KEY).decode('utf-8')
#             print(token)
#         return Response(status=status.HTTP_200_OK)


# # from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated

# # from rest_framework.response import Response
# # from rest_framework.views import APIView


class ExampleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            "user": str(request.user),  # `django.contrib.auth.User` instance.
            "auth": str(request.auth),  # None
        }
        return Response(content)

class Sign(serializers.ModelSerializer):
    class Meta:
        model=User_Auth
        fields="__all__"
        # extra_kwargs = {"password": {"write_only": True}}

class SignView(APIView):

    serializer_class=Sign
    def post(self,request):
        serializer=Sign(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.error_messages)