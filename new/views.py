from django.shortcuts import render





from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from new.models import NewJson
from new.serializers import NewJsonSerializer

def exampleView(request):
    return render(request,'example.html')



@api_view(["POST"])
def snippets_list(request):

    if request.method == "GET":
        snippets = NewJson.objects.all()
        serializer = NewJsonSerializer(snippets,many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = NewJsonSerializer(data=request.data,many=False)
        if serializer.is_valid():
   
            serializer.save()
            request_data=serializer.data
            NewJson.objects.get_or_create(
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