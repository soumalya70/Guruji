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
        model=GurujiWords
        fields= '__all__'
class Todays_UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todays_Updates
        fields='__all__'
class Aj_ka_RashifalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Aaj_ka_Rashifal
        fields='__all__'
class FestivalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Festival
        fields='__all__'

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model=Testimonial
        fields='__all__'
    
class Testimonial_statusSerializer(serializers.ModelSerializer):
    class Meta:
        model=Testimonial_status
        fields='__all__'
        
class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Footer
        fields='__all__'