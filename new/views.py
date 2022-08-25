from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from new.models import NewJson
from new.serializers import NewJsonSerializer
from rest_framework.exceptions import APIException


def exampleView(request):
    return render(request, "example.html")


@api_view(["POST"])
def snippets_list(request):

    # if request.method == "GET":
    #     snippets = NewJson.objects.all()
    #     serializer = NewJsonSerializer(snippets, many=True)
    #     return Response(serializer.data)

    if request.method == "POST":
        serializer = NewJsonSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            request_data = serializer.data
            for i in range(len(request_data)):
                request_data = serializer.data
                NewJson.objects.create(
                    _id=request_data[i]["_id"],
                    altitudeAccuracy=request_data[i]["coords"]["altitudeAccuracy"],
                    accuracy=request_data[i]["coords"]["accuracy"],
                    speed=request_data[i]["coords"]["speed"],
                    altitude=request_data[i]["coords"]["altitude"],
                    heading=request_data[i]["coords"]["heading"],
                    latitude=request_data[i]["coords"]["latitude"],
                    longitude=request_data[i]["coords"]["longitude"],
                    timestamp=request_data[i]["timestamp"],
                    mocked=request_data[i]["mocked"],
                    _v=request_data[i]["_v"],
                    updatedAt=request_data[i]["updatedAt"],
                    createdAt=request_data[i]["createdAt"],
                )
            return Response(status=status.HTTP_200_OK)
        error = Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        print(error.data)
        return error
    if request.method != "POST":
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
