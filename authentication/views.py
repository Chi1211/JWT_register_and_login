from django.shortcuts import render
from .serializers import RegisterSerializer, LoginSerializer, ChangepasswordSerializer, ChangeProfileSerializer,  AccessToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import login
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
from rest_framework import status
# from django.contrib.auth.models import User
from .models import User
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
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
        refresh=AccessToken.for_user(user)
        respone={
            "id":user.id,
            "username":user.username,
            "status_code": 200,
            # "refresh": str(refresh),
            # "acccess": str(refresh.access_token),
            "access": str(refresh)
            
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
    def get(self, request):
        username=request.data['username']
        user=User.objects.get(username=username)  
        serializer=ChangeProfileSerializer(user)
        if serializer:
            response={
                # "username":user.username,
                # "email":user.email,
                # "last_name":user.last_name,
                # "first_name":user.first_name,
                # "address":user.address,
                # "avatar":user.avatar,
                "user":serializer.data,
                "status_code": 200
            }
            return Response(response, status=200)
        return Response({"detai":"error"}, status=400)
    def put(self, request):
        username=request.data['username']
        user=User.objects.get(username=username)
        serializer=ChangeProfileSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response={
                # "username":user.username,
                # "email":user.email,
                # "last_name":user.last_name,
                # "first_name":user.first_name,
                # "address":user.address,
                # "avatar":user.avatar,
                "user":serializer.data,
                "status_code": 200
            }
            return Response(response, status=200)
        return Response(serializer.errors, status=400)
        
class LogoutView(APIView):
    permission_classes=(IsAuthenticated,)
    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)
        return Response(status=status.HTTP_204_NO_CONTENT)



class CheckToken(APIView):
    # permission_classes=(AllowAny,)
    def get(self, request):
        access=request.data['access']
        # if AccessToken(access).check_blacklist() =='a':
        #     return Response({"token":"token is invalid", "status_code": 403}, status= 403)
        # # print(AccessToken(access).check_blacklist(), 'self')
        if AccessToken(access).check_blacklist():
            return Response({"token":"token in blacklisted", "status_code": 403}, status= 403)
        return Response({"token":access, "status_code": 200}, status=200)