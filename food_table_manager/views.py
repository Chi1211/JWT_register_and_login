from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CategoriesModel, FoodModel
from .serializers import CategoriesSerializer, FoodSerializer
from rest_framework import status
# Create your views here.
class GetCategoriesView(APIView):
    def get(self, request):
        unit=CategoriesModel.objects.all()
        serializer = CategoriesSerializer(unit, many=True)
        response={
            "data": serializer.data,
            "status_code": status.HTTP_200_OK,
        }
        return Response(response, status=status.HTTP_200_OK)

class CreateFoodView(APIView):
    def get(self, request):
        food=FoodModel.objects.all()
        serializer = FoodSerializer(material, many=True)
        response={
            "data": serializer.data,
            "status_code": status.HTTP_200_OK,
        }
        return Response(response, status=status.HTTP_200_OK)
    def post(self, request):
        serializer=FoodSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response={
           'data': serializer.data,
           'status_code': status.HTTP_201_CREATED
        }
        return Response(response, status=status.HTTP_201_CREATED)