from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
import json
from googleapiclient.discovery import build
from oauth2client import client
from django.views.decorators.csrf import csrf_exempt
from urllib import parse
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework import status


# class GoogleLogin(
#     SocialLoginView
# ):  # if you want to use Authorization Code Grant, use this
#     adapter_class = GoogleOAuth2Adapter
#     callback_url = "http://localhost:8000"
#     client_class = OAuth2Client


def home(request):
    return render(request, "json.html")


class GoogleLogin(SocialLoginView):  # if you want to use Implicit Grant, use this
    adapter_class = GoogleOAuth2Adapter


from . import settings
import requests
from rest_framework.validators import ValidationError

GOOGLE_AUTH_URL = "https://www.googleapis.com/oauth2/v4/token"


@csrf_exempt
def calender(request):
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)
    code = body["code"]
    data = {
        "code": code,
        "client_id": "917537609153-lpfjkd2e0ca4otak7focgqs1mbv7g2ut.apps.googleusercontent.com",
        "client_secret": "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",
        "redirect_uri": "http://localhost:8000",
        "grant_type": "authorization_code",
    }
    response = requests.post(GOOGLE_AUTH_URL, data=data)
    credentials = response.json()
    if not response.ok:
        raise ValidationError("Failed to obtain access token from Google.")
    print(credentials)
    access_token = response.json()["access_token"]

    return access_token


def refresh_token():
    cred = {
        "access_token": "ya29.a0Aa4xrXP8tOja_f1kUpRthp11YQib99WSGgF1Ync9Dq-h8zAU5-9JfVwbmLKIseIS0Fpx_VSfk0dwBVXSlmPd21_Prjp-QirgNIstq5-rCUj4ZWvmXMwvFM4QIWzWgXQK8zMjaqNh2Aa6RyGnKoAd7Gk0xY8vaCgYKATASARESFQEjDvL90qfALY0YEtxBnNnuibJd4A0163",
        "expires_in": 3598,
        "scope": "openid https://www.googleapis.com/auth/calendar.events https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email",
        "token_type": "Bearer",
        "id_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjIwOWMwNTdkM2JkZDhjMDhmMmQ1NzM5Nzg4NjMyNjczZjdjNjI0MGYiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiI5MTc1Mzc2MDkxNTMtbHBmamtkMmUwY2E0b3Rhazdmb2NncXMxbWJ2N2cydXQuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiI5MTc1Mzc2MDkxNTMtbHBmamtkMmUwY2E0b3Rhazdmb2NncXMxbWJ2N2cydXQuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMTQxMjI3NDI1NTU4MzI2MDkwMzYiLCJlbWFpbCI6InNoYWlrbW9oYW1tZWRpbGl5YXM4MzdAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImF0X2hhc2giOiItZlBTb0Q2T1pJcnBsUU9vdlpPaUh3IiwibmFtZSI6IklMSVlBUyBTSEFJSyIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQUNOUEV1OGh0MlJxZlZVT2ZNV2VsX05rdmFfNHQwanZYREQtS2xLdnZnM3J6U2s9czk2LWMiLCJnaXZlbl9uYW1lIjoiSUxJWUFTIiwiZmFtaWx5X25hbWUiOiJTSEFJSyIsImxvY2FsZSI6ImVuIiwiaWF0IjoxNjYzODUyNTU3LCJleHAiOjE2NjM4NTYxNTd9.katm70TGn8xRc8yYcz8CXGmBQZkLXg4fxjgKebPfuaEkncIzch9BVMXYuGbFbAO38NAiornGWQ83YAEM9REF7H5AyvAZOt2l25ZB9nJVJdipbzs4tI2IjapamnaUcvBuUjyE_s2kpNcMFi3slikBVzCft1FoVF9J-RGRZQekndl0kX4-BK2n-ecQj_369QF_Rn4R-gy6XiO5x7WSWRENbTOdNJiVHRFLs5nJhaufk2vE90inJQ44MxIChaKIy2j0PrBw_VQqMcekBQOT_qEwPF_k-cfajCUzQvC_K9_xeQPL22amUtR9toySBu2N77OB-6WSv8_c7Agai-aX_Yr-7w",
    }
    cred.re

    # test_url = "http://localhost:8000/?" + content
    # print(test_url)
    # if parse.parse_qs(parse.urlparse(test_url).query)["refresh_token"][0]!=None:
    #    refresh_token=parse.parse_qs(parse.urlparse(test_url).query)["refresh_token"][0]
    #    print(refresh_token)
    # access_token = parse.parse_qs(parse.urlparse(test_url).query)["access_token"][0]
    # token_type = parse.parse_qs(parse.urlparse(test_url).query)["token_type"][0]
    # expires_in = parse.parse_qs(parse.urlparse(test_url).query)["expires_in"][0]
    # scopes = parse.parse_qs(parse.urlparse(test_url).query)["scope"][0]
    # json_credentials = {
    #     "access_token": access_token,
    #     "token_type": token_type,
    #     "expires_in": expires_in,
    #     "scope": scopes,
    # }
    # print(json_credentials)
    # credentials = client.AccessTokenCredentials(access_token, "USER_AGENT")
    # service = build("calendar", "v3", credentials=credentials)
    # google_calendar_events = (
    #     service.events()
    #     .list(calendarId="primary", singleEvents=True, orderBy="startTime")
    #     .execute()
    # )
    # google_calendar_events = google_calendar_events.get("items", [])
    # if not google_calendar_events:
    #     print("No upcoming events found.")
    #     return Response(
    #         data={"message": "no events"}, status=status.HTTP_204_NO_CONTENT
    #     )
    # # Prints the start and name of the next 10 events
    # for event in google_calendar_events:
    #     start = event["start"].get("dateTime", event["start"].get("date"))
    #     # return Response(data={"data": start}, status=status.HTTP_200_OK)
    #     # print(start, event["summary"])
    # return JsonResponse({"events": google_calendar_events}, status=status.HTTP_200_OK)


from events.views import GoogleCalendarInitView, GoogleCalendarRedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
    path("rest/v1/calendar/init/", GoogleCalendarInitView),
    path("rest/v1/calendar/redirect/", GoogleCalendarRedirectView),
    path("calender/", include("events.urls")),
    path("u/", include("users.urls")),
    path("dj-rest-auth/google/", GoogleLogin.as_view(), name="google_login"),
    path("calender/", calender),
]
