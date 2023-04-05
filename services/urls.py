from django.urls import path
from .views import *

urlpatterns = [
    path('cards', ServiceCardAPIView.as_view(), name='Gurujiapi'),
    path('cards/<int:id>/', ServiceCardDetailAPIView.as_view(), name='card_detail_api'),
]