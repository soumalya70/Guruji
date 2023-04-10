from django.urls import path
from .views import *

urlpatterns = [
    path('blog', BlogAPIView.as_view(), name='Blogapi'),
    path('blog/<int:id>', BlogIdAPIView.as_view(), name='Blog_id_api'),
#     path('Nature', NatureAPIView.as_view(), name='Nature-api'),
#     path('political',PoliticalAPIView.as_view(), name='political-api'),
#     path('sports',SportAPIView.as_view(), name='sports-api'),
#     path('social',SocialAPIView.as_view(), name='social-api'),
#     path('Religious',ReligiousAPIView.as_view(), name='rel'),
]