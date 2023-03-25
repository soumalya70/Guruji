from django.contrib import admin
from .models import *
# Register your models here.
class HeadingAdmin(admin.ModelAdmin):
    list_display = ('image', 'heading')

class TopImageAdmin(admin.ModelAdmin):
    list_display = ('description',)
    fieldsets = (
        (None, {
            'fields': ('description', 'image1', 'image2', 'image3')
        }),
    )

class SecondTopImageAdmin(admin.ModelAdmin):
    list_display = ('description',)
    fieldsets = (
        (None, {
            'fields': ('description', 'image')
        }),
    )

class MeetGurujiAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time')
    fieldsets = (
        (None, {
            'fields': ('title', 'date', 'time', 'image')
        }),
    )

class LatestFromGurujiAdmin(admin.ModelAdmin):
    list_display = ('book', 'image')

class AboutOtherPartAdmin(admin.ModelAdmin):
    list_display = ('heading', 'description', 'image', 'background_image', 'types_details', 'addon_image1', 'addon_image2', 'addon_image3')

admin.site.register(Heading, HeadingAdmin)
admin.site.register(TopImage, TopImageAdmin)
admin.site.register(SecondTopImage, SecondTopImageAdmin)
admin.site.register(MeetGuruji, MeetGurujiAdmin)
admin.site.register(LatestFromGuruji, LatestFromGurujiAdmin)
admin.site.register(AboutOtherPart, AboutOtherPartAdmin)
