from django.contrib import admin
from .models import *

class AstrologyAdmin(admin.ModelAdmin):
    list_display=('title', 'description')
class NatureAdmin(admin.ModelAdmin):
    list_display=('title', 'description')
class PoliticalAdmin(admin.ModelAdmin):
    list_display=('title', 'description')
class SportsAdmin(admin.ModelAdmin):
    list_display=('title', 'description')
class SocialAdmin(admin.ModelAdmin):
    list_display=('title', 'description')
class ReligiousAdmin(admin.ModelAdmin):
    list_display=('title', 'description')

admin.site.register(Astrology, AstrologyAdmin)
admin.site.register(Nature,NatureAdmin)
admin.site.register(Political,PoliticalAdmin)
admin.site.register(Sports,SportsAdmin)
admin.site.register(Social,SocialAdmin)
admin.site.register(Religious,ReligiousAdmin)
