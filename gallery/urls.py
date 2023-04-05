from django.urls import path
from .views import *

urlpatterns = [
    path('add-photo', Add_photoAPIView.as_view(), name='add_photoapi'),
    path('add-video', Add_videoAPIView.as_view(), name='add_videoapi'),
]
