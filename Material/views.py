from django.shortcuts import render
from rest_framework.response import Response
from .serializers import MaterialSerializer, UnitSerializer
from .models import MaterialModel, UnitModel
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework import generics
# Create your views here.


class GetUnitView(generics.ListAPIView):
    # def get(self, request):
    queryset=UnitModel.objects.all()
    serializer_class=UnitSerializer
        # response={
        #     "data": serializer.data,
        #     "status_code": status.HTTP_200_OK,
        # }
        # return Response(response, status=status.HTTP_200_OK)

class CreateMaterialView(APIView):
    permission_classes=(AllowAny,)
    def get(self, request):
        materia=MaterialModel.objects.all()
        serializer = MaterialSerializer(materia, many=True)
        response={
            "data": serializer.data,
            "status_code": status.HTTP_200_OK,
        }
        return Response(response, status=status.HTTP_200_OK)
    def post(self, request):
        serializer=MaterialSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response={
           'data': serializer.data,
           'status_code': status.HTTP_201_CREATED
        }
        return Response(response, status=status.HTTP_201_CREATED)
        
class UpdateMaterialView(APIView):
    permission_classes=(AllowAny,)
    def get_object(self, pk):
        try: 
            material=MaterialModel.objects.get(pk=pk)
            return supplier
        except MaterialModel.DoesNotExist:
            return Response({"errors":"errors"}, status=404)
    def get(self, request, pk):
        material=self.get_object(pk)
        serializer=MaterialSerializer(material)
        
        response={
            "data": serializer.data,
            "status_code": 200
        }
        return Response(response, status=200)
    def put(self, renquest, pk):
        material=self.get_object(pk)
        serializer=MaterialSerializer(material, data=renquest.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response={
            'data': serializer.data,
            'status_code': status.HTTP_200_OK
        }
        return Response(response, status=status.HTTP_200_OK)

class SearchMaterialView(APIView):
    permission_classes=(AllowAny,)
    def get(self, request):
        name=request.data["supplier_name"]
        material=MaterialModel.objects.filter(material_name__contains=name)
        serializer = MaterialSerializer(material, many=True)
        response={
            "data": serializer.data,
            "status_code": status.HTTP_200_OK,
        }
        return Response(response, status=status.HTTP_200_OK)