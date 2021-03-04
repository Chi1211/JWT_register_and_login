from django.shortcuts import render
from .serializers import RegisterSerializer, LoginSerializer, ChangepasswordSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import login
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
from django.contrib.auth.models import User
# Create your views here.
class RegisterView(APIView):
    permission_classes=(IsAuthenticated,)

    def post(self, request):
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            response={
                "username": user.username,
                'status_code':201,
            }
            return Response(response, status=201)
        return Response(serializer.errors, status=400)


class LoginView(APIView):
    permission_classes=(AllowAny,)

    def post(self, request):
        serializer=LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user=serializer.validated_data['user']
        login(request, user)
        refresh=RefreshToken.for_user(user)
        respone={
            "id":user.id,
            "username":user.username,
            "status_code": 200,
            "token": str(refresh.access_token),
            
        }

        return Response(respone, status=200)

class ChangePasswordView(APIView):
    permission_classes=(IsAuthenticated,)  
    def put(self, request):
        password=request.data['password']
        username=request.data['username']
        user=User.objects.get(username=username)
        serializer = ChangepasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(password)
            user.save()
            response={
                'username':user.username,
                'password':user.password,
                'status_code':200
            }
            return Response(response, status=200)
        return Response(serializer.errors, status=400)


class ChangeProfileView(APIView):
    permission_classes=(IsAuthenticated,)  
    def put(self, request):
        username=request.data['username']
        user=User.objects.get(username=username)
        serializer = ChangepasswordSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)




