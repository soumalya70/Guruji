from django.urls import path
from .views import *

urlpatterns = [
    path('home/banner-image/', BannerImageAPIView.as_view(), name='banner-image-api'),
    path('home/aboutguruji/', AboutGurujiAPIView.as_view(), name='aboutguruji-api'),
    path('home/our-services-cards/',OurServiceAPIView.as_view(),name='our-service-cards-api'),
    path('home/resolve-problems/',ResolveProblemsAPIView.as_view(),name='resolve-problems-api'),
    path('home/guruji-words/',GurujWordsAPIView.as_view(),name='guruji-words-api'),
]
