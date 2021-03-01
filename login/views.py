from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserLoginSerializer
from rest_framework import permissions
from django.contrib.auth.models import User
from django.contrib.auth import login
from rest_framework_simplejwt.tokens import RefreshToken

class UserLogin(APIView):
    permission_classes=([permissions.AllowAny,])

    def post(self, request):
        serializer=UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user=serializer.validated_data['user']
        login(request, user)
        refresh=RefreshToken.for_user(user)
        respone={
            "username":user.username,
            "password":user.password,
            "status_code": 200,
            # "refresh": str(refresh),
            "acccess": str(refresh.access_token),
            
        }

        return Response(respone, status=200)