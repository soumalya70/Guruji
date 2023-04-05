from django.contrib import admin
from .models import *

# Register your models here.
class CardAdmin(admin.ModelAdmin):
    list_display = ('image', 'heading', 'description')
admin.site.register(Card,CardAdmin)

# class DescriptionAdmin(admin.ModelAdmin):
#     list_display=('text', 'image', 'description')
# admin.site.register(Description,DescriptionAdmin)