from django.shortcuts import render
from django.contrib.auth.models import User
from .serializer import UserRegisterSerializer
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView


# Create your views here.

class UserRegister(APIView):
    permission_classes=([permissions.AllowAny])
    def post(self, request):
        serializer=UserRegisterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        user=serializer.save()
        refresh=RefreshToken.for_user(user)
        res={
            "refresh": str(refresh),
            "acccess": str(refresh.access_token),
        }
        return Response(res, status=200)