from rest_framework import serializers
from .models import MaterialModel


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model=MaterialModel
        fields='__all__'