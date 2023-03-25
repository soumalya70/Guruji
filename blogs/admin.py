from django.contrib import admin
from .models import Blog, Card


class CardAdmin(admin.ModelAdmin):
    list_display=('image', 'description')



class BlogAdmin(admin.ModelAdmin):
    list_display=('image', 'heading', 'description', 'detail_description', 'background_image', 'youtube_link')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Card,CardAdmin)
