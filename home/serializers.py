from rest_framework import serializers
from .models import *

class BannerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerImage
        fields = '__all__'
class AboutGurujiSerializer(serializers.ModelSerializer):
    class Meta:
        model= AboutGuruji
        fields= '__all__'
class OurservicesCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Our_Services_Cards
        fields='__all__'
class ResolveProblemsSerializer(serializers.ModelSerializer):
    class Meta:
        model= ResolveProblem
        fields='__all__'
    
class GurujiWordsSerializer(serializers.ModelSerializer):
    class Meta:
        models=GurujiWords
        fields= '__all__'