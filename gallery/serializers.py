from rest_framework import serializers
from .models import *

class Add_photoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Add_Photo
        fields='__all__'
        
class Add_videoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Add_video
        fields='__all__'