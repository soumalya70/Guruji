from django.contrib import admin
from .models import *

# Register your models here.
class CardAdmin(admin.ModelAdmin):
    list_display = ('heading', 'image', 'description','long_description')
admin.site.register(Card,CardAdmin)

# class DescriptionAdmin(admin.ModelAdmin):
#     list_display=('text', 'image', 'description')
# admin.site.register(Description,DescriptionAdmin)