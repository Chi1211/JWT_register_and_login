from django.urls import path
from . import views
urlpatterns=[
    path('category/', views.GetCategoriesView.as_view(), name='get_category'),
]