from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class UserLoginSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=255)
    password=serializers.CharField(max_length=255, write_only=True)

    def validate(self, validate_data):
        username=validate_data.get("username", None)
        password=validate_data.get("password", None)
        user=authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError({"username":"username and password do not exists"})
        validate_data['user']=user
        return validate_data