from rest_framework import generics
from .models import *
from .serializers import *
class BannerImageAPIView(generics.ListAPIView):
    queryset = BannerImage.objects.all().order_by('-id')[:1]
    serializer_class = BannerImageSerializer

class AboutGurujiAPIView(generics.ListAPIView):
    queryset = AboutGuruji.objects.all().order_by('-id')[:1]
    serializer_class = AboutGurujiSerializer

class OurServiceAPIView(generics.ListAPIView):
    queryset = Our_Services_Cards.objects.all()
    serializer_class = OurservicesCardsSerializer

class ResolveProblemsAPIView(generics.ListAPIView):
    queryset = ResolveProblem.objects.all().order_by('-id')[:1]
    serializer_class=ResolveProblemsSerializer
    
class GurujWordsAPIView(generics.ListAPIView):
    queryset =GurujiWords.objects.all().order_by('-id')[:3]
    serializer_class=GurujiWordsSerializer
