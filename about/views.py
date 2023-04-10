from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.
class GurujiAPIView(generics.ListAPIView):
    queryset = Guruji.objects.all().order_by('-id')[:1]
    serializer_class = GurujiSerializer

class HoroscopeAPIView(generics.ListAPIView):
    queryset=Horoscope.objects.all().order_by('-id')[:1]
    serializer_class=HoroscopeSerializer

class KundliAPIView(generics.ListAPIView):
    queryset=Kundli.objects.all().order_by('-id')[:1]
    serializer_class=KundliSerializer
    
class GorcharAPIView(generics.ListAPIView):
    queryset=Gorchar.objects.all().order_by('-id')[:1]
    serializer_class=GorchaSerializer
    
class VedicAPIView(generics.ListAPIView):
    queryset=Vedic_astrology.objects.all().order_by('-id')[:1]
    serializer_class=VedicSerializer

                      
                                