from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import User
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=64, min_length=6, write_only=True)
    password2=serializers.CharField(max_length=64, min_length=6,write_only=True)
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
        if password !=password2:
            raise serializers.ValidationError({"password": "password do not match"})

        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        return user

class LoginSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=255)
    password=serializers.CharField(max_length=64, min_length=6, write_only=True)

    class Meta:
        model=User
        fields=['username', 'password']

    def validate(self, validate_data):
        username=validate_data.get("username", None)
        password=validate_data.get("password", None)

        if not User.objects.filter(username=username):
            raise serializers.ValidationError({"username":"username does not exist"})
        user=authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError({"password":"password does not exists"})
        validate_data['user']=user
        return validate_data

class ChangepasswordSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=255)
    password=serializers.CharField(max_length=64, min_length=6, write_only=True)
    confirm_password=serializers.CharField(max_length=64, min_length=6,write_only=True)
    password_old=serializers.CharField(max_length=64, min_length=6,write_only=True)

    class Meta:
        model=User
        fields=['username', 'password','confirm_password','password_old']

    def validate(self, validate_data): 
        username=validate_data.get('username', None)
        password=validate_data.get('password', None)
        confirm_password=validate_data.get('confirm_password', None)
        password_old=validate_data.get('password_old', None)        
        if password_old == password:
            raise serializers.ValidationError({"detail": "the new password is the same as the old one"})
        user=authenticate(username=username, password=password_old)
        if not user:
            raise serializers.ValidationError({"password_old": "old password is not correct", "password":user.password})    
        if password !=confirm_password:
            raise serializers.ValidationError({"password": "password do not match"})
        return validate_data

class ChangeProfileSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=255)
    email=serializers.CharField(max_length=255)
    address=serializers.CharField(max_length=255)

    class Meta:
        model=User
        fields=['username', 'email', 'last_name', 'first_name', 'address', 'avatar']

    def update(self, instance, validate_data):
        username=validate_data.get('username', None)
        email=validate_data.get('email', None)
        # if User.objects.filter(email=email) and :
        #     raise serializers.ValidationError({"email": "email already exists"})

        instance.last_name = validate_data.get('last_name', instance.last_name)
        instance.first_name = validate_data.get('first_name', instance.first_name)
        instance.email = validate_data.get('email', instance.email)
        instance.address = validate_data.get('address', instance.address)
        instance.avatar = validate_data.get('avatar', instance.avatar)
        instance.save()
        return instance

    


