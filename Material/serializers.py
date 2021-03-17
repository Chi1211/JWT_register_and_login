from rest_framework import serializers
from .models import MaterialModel, ImportMaterialModel


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model=MaterialModel
        fields='__all__'

class ImportMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model=ImportMaterialModel
        fields='__all__'
