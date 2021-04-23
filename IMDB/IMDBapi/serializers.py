from .models import IMDBdata
from rest_framework import serializers

class IMDBSerializer(serializers.ModelSerializer):
    class Meta:
        model = IMDBdata
        fields = ['Title', 'Year', 'Rating', 'ImgUrl']