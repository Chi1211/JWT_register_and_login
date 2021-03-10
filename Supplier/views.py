from django.shortcuts import render
from .serializer import SupplierSerialier
from .models import SupplierModel
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
# Create your views here.

class CreateSupplierView(APIView):
    permission_classes=(AllowAny,)
    def get(self, request):
        supplier=SupplierModel.objects.all()
        serializer = SupplierSerialier(supplier, many=True)
        response={
            "data": serializer.data,
            "status_code": status.HTTP_200_OK,
        }
        return Response(response, status=status.HTTP_200_OK)
    def post(self, request):
        serializer=SupplierSerialier(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response={
           'data': serializer.data,
           'status_code': status.HTTP_201_CREATED
        }
        return Response(response, status=status.HTTP_201_CREATED)
        
class UpdateSupplierView(APIView):
    permission_classes=(AllowAny,)
    def get_objects(self, pk):
        try: 
            supplier=SupplierModel.objects.get(pk=pk)
        except SupplierModel.DoesNotExist:
            return Response({"errors":"errors"}, status=404)
    def get(self, request, pk):
        supplier=self.get_objects(pk)
        serializer=SupplierSerialier(supplier)
        response={
            "data": serializer.data,
            "status_code": 200
        }
        return Response(response, status=200)
