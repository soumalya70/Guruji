from django.urls import path
from .views import *

urlpatterns = [
    path('guruji', GurujiAPIView.as_view(), name='Gurujiapi'),
    path('horoscope', HoroscopeAPIView.as_view(), name='Horoscopeapi'),
    path('kundli', KundliAPIView.as_view(), name='KundliAPI'),
    path('gorchar', GorcharAPIView.as_view(), name='GorcharAPI'),
    path('vedic', VedicAPIView.as_view(), name='Vedicapi'),
]  