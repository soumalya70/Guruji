from rest_framework import generics
from .models import *
from .serializers import *
class BannerImageAPIView(generics.ListCreateAPIView):
    queryset = BannerImage.objects.all().order_by('-id')[:1]
    serializer_class = BannerImageSerializer

class AboutGurujiAPIView(generics.ListCreateAPIView):
    queryset = AboutGuruji.objects.all().order_by('-id')[:1]
    serializer_class = AboutGurujiSerializer

class OurServiceAPIView(generics.ListCreateAPIView):
    queryset = Our_Services_Cards.objects.all()
    serializer_class = OurservicesCardsSerializer

class ResolveProblemsAPIView(generics.ListCreateAPIView):
    queryset = ResolveProblem.objects.all().order_by('-id')[:1]
    serializer_class=ResolveProblemsSerializer
    
class GurujWordsAPIView(generics.ListCreateAPIView):
    queryset =GurujiWords.objects.all().order_by('-id')[:3]
    serializer_class=GurujiWordsSerializer
