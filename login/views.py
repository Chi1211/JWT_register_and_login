from django.shortcuts import render
from .serializer import UserLoginSerializer
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth import login
from rest_framework.renderers import TemplateHTMLRenderer
# Create your views here.

class UserLogin(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'
    permission_classes=([permissions.AllowAny,])
    def get(self, request):
        return render(request, "login/login.html")
    def post(self, request):
        serializer=UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        refresh=RefreshToken.for_user(user)
        login(request, user)
        response={
            "username": user.username,
            "password":user.password,
            'status_code' : status.HTTP_200_OK,
            "refresh": str(refresh),
            "acccess": str(refresh.access_token),
        }

        return Response(response, status=200)