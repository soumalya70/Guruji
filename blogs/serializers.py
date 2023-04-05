from rest_framework import serializers
from .models import *

class AstrologySerializer(serializers.ModelSerializer):
    class Meta:
        model=Astrology
        fields='__all__'
class NaturesSerializer(serializers.ModelSerializer):
    class Meta:
        models=Nature
        fields='__all__'
class PoliticalSerializer(serializers.ModelSerializer):
    class Meta:
        models=Political
        fields='__all__'
class SportsSerializer(serializers.ModelSerializer):
    class Meta:
        models=Sports
        fields='__all__'
class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        models=Social
        fields='__all__'
class ReligiousSerializer(serializers.ModelSerializer):
    class Meta:
        models=Religious
        fields='__all__'        