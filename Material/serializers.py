from rest_framework import serializers
from .models import UnitModel, MaterialModel

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model=UnitModel
        fields='__all__'

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model=MaterialModel
        fields='__all__'