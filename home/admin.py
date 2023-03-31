from django.contrib import admin
from .models import *

class BannerImageAdmin(admin.ModelAdmin):
    list_display = ('banner_description', 'banner_background', 'banner_image')

admin.site.register(BannerImage, BannerImageAdmin)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('description','image' )

admin.site.register(AboutGuruji, AboutAdmin)
class Our_Services_CardsAdmin(admin.ModelAdmin):
    list_display = ('title','image','description')

admin.site.register(Our_Services_Cards, Our_Services_CardsAdmin)

class Todays_update_CardAdmin(admin.ModelAdmin):
    list_display = ('nakshatra','image' , 'tithi','sunrise','sunset','yoga','rashi','description','todays_update')
admin.site.register(Todays_Updates,Todays_update_CardAdmin)

class ResolveProblemAdmin(admin.ModelAdmin):
    list_display = ('description', 'image')

admin.site.register(ResolveProblem, ResolveProblemAdmin)

class GurujiWordsAdmin(admin.ModelAdmin):
    list_display = ('image', 'heading', 'description')

admin.site.register(GurujiWords, GurujiWordsAdmin)

class Aaj_ka_RasidalAdmin(admin.ModelAdmin):
    list_display = ('Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces')

admin.site.register(Aaj_ka_Rashifal, Aaj_ka_RasidalAdmin)

class FestivalAdmin(admin.ModelAdmin):
    list_display = ('date', 'description')

admin.site.register(Festival, FestivalAdmin)

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('image', 'description', 'name', 'designation')

admin.site.register(Testimonial, TestimonialAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('date', 'address')

admin.site.register(Appointment,AppointmentAdmin)

class FooterAdmin(admin.ModelAdmin):
    list_display = ('contact_no', 'email_id', 'Address', 'facebook', 'instagram', 'twitter')

admin.site.register(Footer,FooterAdmin)

class Testimonial_StatusAdmin(admin.ModelAdmin):
    list_display = ('Happy_Clients', 'Services_Available', 'Happy_Family')
admin.site.register(Testimonial_status,Testimonial_StatusAdmin)
