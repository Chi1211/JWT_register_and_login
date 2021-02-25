from django.urls import path
from . import views
urlpatterns=[
    path('sign/', views.UserLogin.as_view(), name="login" )
]