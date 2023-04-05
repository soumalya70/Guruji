from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
# Create your views here.

class Add_photoAPIView(generics.ListCreateAPIView):
    queryset = Add_Photo.objects.all()
    serializer_class = Add_photoSerializer

class Add_videoAPIView(generics.ListCreateAPIView):
    queryset=Add_video.objects.all()
    serializer_class=Add_videoSerializer