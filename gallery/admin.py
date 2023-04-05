from django.contrib import admin
from .models import *
# Register your models here.
class Add_videoAdmin(admin.ModelAdmin):
    list_display = ('video_template', 'video_link')
admin.site.register(Add_Photo)
admin.site.register(Add_video,Add_videoAdmin)