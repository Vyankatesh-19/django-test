from rest_framework import serializers
from .models import MagazineInfo, MagazineContent

# Serializer for MagazineContent
class MagazineContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MagazineContent
        fields = '__all__' 

# Serializer for MagazineInfo
class MagazineInfoSerializer(serializers.ModelSerializer):
    contents = MagazineContentSerializer(many=True, read_only=True)  # Nested content

    class Meta:
        model = MagazineInfo
        fields ='__all__' 
