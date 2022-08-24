import requests
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from apijson.models import Ancestor, NewApiJsonData # ApiJsonData, JsonData, JsonDataModel,
from apijson.serializers import ApiJsonSerializer, JsonSerializer #, JsonDataSerializer


@permission_classes([IsAuthenticated])
def jsonData(request):
    return render(request, "json.html")


@api_view(["GET", "POST"])
def snippet_list(request):

    if request.method == "GET":
        snippets = NewApiJsonData.objects.all()
        serializer = ApiJsonSerializer(snippets,many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = ApiJsonSerializer(data=request.data,many=False)
        if serializer.is_valid():
   
            serializer.save()
            request_data=serializer.data
            print(request_data)
            Ancestor.objects.get_or_create(
            _id=request_data["_id"],
            altitudeAccuracy=request_data["coords"]["altitudeAccuracy"],
            accuracy=request_data["coords"]["accuracy"],
            speed=request_data["coords"]["speed"],
            altitude=request_data["coords"]["altitude"],
            heading=request_data["coords"]["heading"],
            latitude=request_data["coords"]["latitude"],
            longitude=request_data["mocked"],
            timestamp=request_data["timestamp"],
            mocked=request_data["mocked"],
            _v=request_data["_v"],
            updatedAt=request_data["updatedAt"],
            createdAt=request_data["createdAt"],
        ) 
            return Response(serializer.data, status=status.HTTP_200_OK)
        error = Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        print(error.data)
        return error


# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
# @api_view(["GET", "POST"])
# def jsonDataInputInDB(request, *args, **kwargs):
#     # false = False
#     endpoint = "https://tracking-poc-backend.herokuapp.com/api/location/get?limit=10"
#     get_response = requests.get(endpoint)
#     request_data = get_response.json()
#     for i in range(len(request_data["data"])):

#         JsonData.objects.get_or_create(
#             _id=request_data["data"][i]["_id"],
#             altitudeAccuracy=request_data["data"][i]["coords"]["altitudeAccuracy"],
#             accuracy=request_data["data"][i]["coords"]["accuracy"],
#             altitude=request_data["data"][i]["coords"]["altitude"],
#             heading=request_data["data"][i]["coords"]["heading"],
#             latitude=request_data["data"][i]["coords"]["latitude"],
#             longitude=request_data["data"][i]["coords"]["longitude"],
#             speed=request_data["data"][i]["coords"]["speed"],
#             mocked=request_data["data"][i]["mocked"],
#             timestamp=request_data["data"][i]["timestamp"],
#             _v=request_data["data"][i]["__v"],
#             updatedAt=request_data["data"][i]["updatedAt"],
#             createdAt=request_data["data"][i]["createdAt"],
#         )
#     return Response(status=status.HTTP_200_OK)

# @api_view(["GET", "POST"])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
# def getUserData(request):
#             if request.method == "POST":
#                 serializer = UserSerializer(data=request.data)
#                 if serializer.is_valid():
#                    serializer.save()
#                    return Response(serializer.data, status=status.HTTP_200_OK)
#             return Response(status=status.HTTP_200_OK)
