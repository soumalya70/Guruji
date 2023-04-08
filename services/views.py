from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.
class ServiceCardAPIView(generics.ListAPIView):
    queryset = Card.objects.all().order_by('-id')[:6]
    serializer_class = ServiceSerializer
    
class ServiceCardDetailAPIView(generics.RetrieveAPIView):
    queryset = Card.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'id'