from django.shortcuts import render
from .serializer import SupplierSerialier
from .models import SupplierModel
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
# Create your views here.
class ListSupplierView(APIView):
    permission_classes=(AllowAny,)
    def get(self, request):
        supplier=SupplierModel.objects.all()
        serializer = SupplierSerialier(supplier, many=True)
        response={
            "data": serializer.data,
            "status_code": status.HTTP_200_OK,
        }
        return Response(response, status=status.HTTP_200_OK)