from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
# Create your views here.

class BlogAPIView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
class BlogIdAPIView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'id'

# class NatureAPIView(generics.ListAPIView):
#     queryset=Nature.objects.all()
#     serializer_class=NaturesSerializer

# class PoliticalAPIView(generics.ListAPIView):
#     queryset=Political.objects.all()
#     serializer_class=PoliticalSerializer
    
# class SportAPIView(generics.ListAPIView):
#     queryset=Sports.objects.all()
#     serializer_class=SportsSerializer

# class SocialAPIView(generics.ListAPIView):
#     queryset=Social.objects.all()
#     serializer_class=SocialSerializer
# class ReligiousAPIView(generics.ListAPIView):
#     queryset=Social.objects.all()
#     serializer_class=ReligiousSerializer