from django.urls import path
from . import views

urlpatterns=[
    path('list_supplier', views.ListSupplierView.as_view(), name="list_supplier"),
]