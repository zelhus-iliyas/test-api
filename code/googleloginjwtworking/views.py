import json
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404, redirect, render
import os.path
from datetime import datetime

import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from .models import Client
from .serializers import ClientSerializer



class CreateClient(APIView):
    serializer_class = ClientSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request):
        request_data = request.data
        serializer = ClientSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetClient(APIView):
    serializer_class = ClientSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request, pk):
        client = get_object_or_404(Client, pk=pk)
        serializer = self.serializer_class(instance=client)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class GetClientList(APIView):
    serializer_class = ClientSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):
        clients = Client.objects.all()
        serializer = self.serializer_class(instance=clients, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UpdateClient(APIView):
    serializer_class = ClientSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request, pk):
        client = Client.objects.get(pk=pk)
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteClient(APIView):
    serializer_class = ClientSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def delete(self, request, pk):
        client = get_object_or_404(Client, pk=pk)
        client.delete()
        return Response(status=status.HTTP_200_OK)



