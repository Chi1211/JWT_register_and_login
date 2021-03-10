from rest_framework import serializers
from .models import MaterialModel, UnitModel

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model=MaterialModel
        fields='__all__'

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model=UnitModel
        fields='__all__'