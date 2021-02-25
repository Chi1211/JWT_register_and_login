from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class UserLoginSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=255)
    password=serializers.CharField(max_length=255)
    # class Meta:
    #     model=User
    #     fields=['username', 'password']
    def validate(self, data):
        username=data.get('username', None)
        password=data.get('password', None)
        user=authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError({"user":"User with given email and password does not exists"})
        else:
            data['user']=user
            return data
