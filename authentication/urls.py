from django.urls import path
from . import views
urlpatterns=[
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('change_pass/', views.ChangePasswordView.as_view(), name='change_pass'),
]
