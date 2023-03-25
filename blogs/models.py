from django.db import models

class Card(models.Model):
    image = models.ImageField(upload_to='blog_cards/')
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description


class Blog(models.Model):
    image = models.ImageField(upload_to='blog_images/')
    heading = models.CharField(max_length=255)
    description = models.TextField()
    detail_description = models.TextField()
    background_image = models.ImageField(upload_to='blog_background_images/')
    youtube_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.heading
