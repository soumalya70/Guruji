from django.contrib import admin
from .models import *

# class AstrologyAdmin(admin.ModelAdmin):
#     list_display=('title', 'description')
class BlogAdmin(admin.ModelAdmin):
    list_display=('title', 'description', 'image', 'title1', 'long_description1', 'title2', 'long_description2')
# class PoliticalAdmin(admin.ModelAdmin):
#     list_display=('title', 'description', 'image', 'title1', 'long_description1', 'title2', 'long_description2')
# class SportsAdmin(admin.ModelAdmin):
#     list_display=('title', 'description', 'image', 'title1', 'long_description1', 'title2', 'long_description2')
# class SocialAdmin(admin.ModelAdmin):
#     list_display=('title', 'description', 'image', 'title1', 'long_description1', 'title2', 'long_description2')
# class ReligiousAdmin(admin.ModelAdmin):
#     list_display=('title', 'description', 'image', 'title1', 'long_description1', 'title2', 'long_description2')

admin.site.register(Blog, BlogAdmin)
# admin.site.register(Nature,NatureAdmin)
# admin.site.register(Political,PoliticalAdmin)
# admin.site.register(Sports,SportsAdmin)
# admin.site.register(Social,SocialAdmin)
# admin.site.register(Religious,ReligiousAdmin)
