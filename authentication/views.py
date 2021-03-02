from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import RegisterSerializer, LoginSerializer
from .renderers import UserJSONRenderer
# Create your views here.

class RegisterView(APIView):
    permission_classes=(AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    def post(self, request):
        serializer=RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

class LoginView(APIView):
    permission_classes=(AllowAny,)
    renderer_classes = (UserJSONRenderer,)

    def post(self, request):
        serializer=LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=200)