from django.contrib.auth import get_user_model
from rest_framework import serializers

User=get_user_model()
class UserRegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True, style={"input_type": "password"})
    password2=serializers.CharField(write_only=True, style={"input_name": "password"})

    class Meta:
        model= User
        fields=['username', 'email', 'password','password2']

        extra_kwargs={"password":{"write_oly":True}}

    def create(self, validate_data):
        username=validate_data["username"]
        email=validate_data["email"]
        password=validate_data["password"]
        password2=validate_data["password2"]

        if User.objects.filter(username=username):
            raise serializers.ValidationError({"username":"usename already exists"})
        if User.objects.filter(email=email):
            raise serializers.ValidationError({"email": "email already exists"})
        if " " in password:
            raise serializers.ValidationError({"password": "password cannot contain spaces"})
        if password !=password2:
            raise serializers.ValidationError({"password": "password do not match"})

        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        return user