from django.db import models
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
# Create your models here.
import jwt

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError({"username":"username must have a username"})
        if username is None:
            raise TypeError({"email":"email must have a email"})

        user=self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user


    def create_superuser(self, username, email, password):
        if username is None:
            raise TypeError({"password":"superuser must have password"})

        user=self.create_user(username, email, password)
        user.is_superuser=True
        user.is_staff=True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username=models.CharField(db_index=True, max_length=255, unique=True)
    email=models.EmailField(db_index=True, unique=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

    objects=UserManager()

    def __str__(self):
        return self.email


    # @property
    def token(self):
        dt=datetime.now()+timedelta(days=5)
        tk=jwt.encode({
            'id':self.id,
            'exp': int(dt.strftime("%S"))
        }, settings.SECRET_KEY, algorithm='HS256')
        return tk

    def get_full_name(self):
        return self.username


    # def _generate_jwt_toexit()ken(self):
        

