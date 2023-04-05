from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
# Create your views here.

class AstrologyAPIView(generics.ListCreateAPIView):
    queryset = Astrology.objects.all()
    serializer_class = AstrologySerializer

class NatureAPIView(generics.ListCreateAPIView):
    queryset=Nature.objects.all()
    serializer_class=NaturesSerializer

class PoliticalAPIView(generics.ListCreateAPIView):
    queryset=Political.objects.all()
    serializer_class=PoliticalSerializer
    
class SportAPIView(generics.ListCreateAPIView):
    queryset=Sports.objects.all()
    serializer_class=SportsSerializer

class SocialAPIView(generics.ListCreateAPIView):
    queryset=Social.objects.all()
    serializer_class=SocialSerializer
class ReligiousAPIView(generics.ListCreateAPIView):
    queryset=Social.objects.all()
    serializer_class=ReligiousSerializer