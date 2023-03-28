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
class Todays_UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        models=Todays_Updates
        fields='__all__'
class Aj_ka_RashifalSerializer(serializers.ModelSerializer):
    class Meta:
        models=Aaj_ka_Rashifal
        fields='__all__'
class FestivalSerializer(serializers.ModelSerializer):
    class Meta:
        models=Festival
        fields='__all__'

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        models=Testimonial
        fields='__all__'
    
class Testimonial_statusSerializer(serializers.ModelSerializer):
    class Meta:
        models=Testimonial_status
        fields='__all__'
        
class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        models=Footer
        fields='__all__'