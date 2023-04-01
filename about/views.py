from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.
class GurujiAPIView(generics.ListCreateAPIView):
    queryset = Guruji.objects.all().order_by('-id')[:1]
    serializer_class = GurujiSerializer

class HoroscopeAPIView(generics.ListCreateAPIView):
    queryset=Horoscope.objects.all().order_by('-id')[:1]
    serializer_class=HoroscopeSerializer

class KundliAPIView(generics.ListCreateAPIView):
    queryset=Horoscope.objects.all().order_by('-id')[:1]
    serializers_class=KundliSerializer
    
class GorcharAPIView(generics.ListCreateAPIView):
    queryset=Gorchar.objects.all().order_by('-id')[:1]
    serializers_class=GorchaSerializer
    
class VedicAPIView(generics.ListCreateAPIView):
    queryset=Vedic_astrology.objects.all().order_by('-id')[:1]
    serializer_class=VedicSerializer

                      
                                