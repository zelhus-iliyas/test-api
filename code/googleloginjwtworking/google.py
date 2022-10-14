import requests

from django.http import HttpResponseRedirect
from django.urls import reverse

from rest_framework.views import APIView

# @api_view(["POST"])
def get_google_login_signup_token(request):
    if request.GET.get("code") != None:
        code = request.GET.get("code")
        response = requests.post("http://localhost:8000/cus/", data={"code": code})
        k = response.json()
        print(k)
        url="http://localhost:8000"
        return HttpResponseRedirect(url)

# class GetGoogleLoginSignupToken(APIView):


