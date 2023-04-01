from django.contrib import admin
from .models import *
# Register your models here.
class GurujiAdmin(admin.ModelAdmin):
    list_display = ('description', 'image', 'guruji_image', 'meet_guruji_image', 'book_image')

class HoroscopeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'title1', 'description1', 'title2', 'description2', 'title3', 'description3', 'title4', 'description4')

class KundliAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'title1', 'description1', 'title2', 'description2', 'title3', 'description3', 'title4', 'description4')

class GorcharAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'title1', 'description1', 'title2', 'description2', 'title3', 'description3', 'title4', 'description4')

class Vedic_astrologyAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'title1', 'description1', 'title2', 'description2', 'title3', 'description3', 'title4', 'description4')

# class AboutOtherPartAdmin(admin.ModelAdmin):
#     list_display = ('heading', 'description', 'image', 'background_image', 'types_details', 'addon_image1', 'addon_image2', 'addon_image3')

admin.site.register(Guruji, GurujiAdmin)
admin.site.register(Kundli, KundliAdmin)
admin.site.register(Horoscope, HoroscopeAdmin)
admin.site.register(Gorchar,GorcharAdmin)
admin.site.register(Vedic_astrology, Vedic_astrologyAdmin)
# admin.site.register(AboutOtherPart, AboutOtherPartAdmin)
