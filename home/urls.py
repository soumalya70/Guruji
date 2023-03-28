from django.urls import path
from .views import *

urlpatterns = [
    path('home/banner-image/', BannerImageAPIView.as_view(), name='banner-image-api'),
    path('home/aboutguruji/', AboutGurujiAPIView.as_view(), name='aboutguruji-api'),
    path('home/our-services-cards/',OurServiceAPIView.as_view(),name='our-service-cards-api'),
    path('home/resolve-problems/',ResolveProblemsAPIView.as_view(),name='resolve-problems-api'),
    path('home/guruji-words/',GurujWordsAPIView.as_view(),name='guruji-words-api'),
    path('home/todays-update/',Todys_UpdatesAPIView.as_view(),name='todays-update-api'),
    path('home/aj-ka-rashifal/',Aj_ka_RashifalAPIView.as_view(),name='aj-ka-rashifal'),
    path('home/festival/',FestivalAPIView.as_view(),name='Festival'), 
    path('home/testimonal',TestimonialAPIView.as_view(),name='testimonial-api'),
    path('home/testimonial-status/',Testimonial_StatusAPIView.as_view(),name='testimonial-status-api'),
    path('home/footer/',FooterAPIView.as_view(),name='footerapi'),
]
