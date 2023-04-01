from rest_framework import serializers
from .models import *

class GurujiSerializer(serializers.ModelSerializer):
    class Meta:
        model=Guruji
        fields='__all__'
        
class HoroscopeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Horoscope
        fields='__all__'

class KundliSerializer(serializers.ModelSerializer):
    class Meta:
        model=Kundli
        fields='__all__'

class GorchaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Gorchar
        fields='__all__'
        
class VedicSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vedic_astrology
        fields='__all__'