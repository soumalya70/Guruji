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

class Todys_UpdatesAPIView(generics.ListCreateAPIView):
    queryset=Todays_Updates.objects.all().order_by('-id')[:1]
    serializer_class=Todays_UpdateSerializer
    
class Aj_ka_RashifalAPIView(generics.ListCreateAPIView):
    queryset=Aaj_ka_Rashifal.objects.all().order_by('-id')[:1]
    serializer_class=Aj_ka_RashifalSerializer

class FestivalAPIView(generics.ListCreateAPIView):
    queryset=Festival.objects.all()
    serializer_class=FestivalSerializer

class TestimonialAPIView(generics.ListCreateAPIView):
    queryset=Testimonial.objects.all().order_by('-id')[:3]
    serializer_class=TestimonialSerializer

class Testimonial_StatusAPIView(generics.ListCreateAPIView):
    queryset=Testimonial_status.objects.all().order_by('-id')[:1]
    serializer_class=Testimonial_statusSerializer
    
class FooterAPIView(generics.ListCreateAPIView):
    queryset=Footer.objects.all().order_by('-id')[:1]
    serializer_class=FooterSerializer