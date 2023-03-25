from django.db import models

# Create your models here.
from django.db import models

class Heading(models.Model):
    image = models.ImageField(upload_to='about/')
    heading = models.CharField(max_length=255)
    def __str__(self):
        return self.heading
    
class TopImage(models.Model):
    image_1 = models.ImageField(upload_to='top_image/')
    image_2 = models.ImageField(upload_to='top_image/')
    image_3 = models.ImageField(upload_to='top_image/')
    description = models.TextField()
    def __str__(self):
        return self.description

class SecondTopImage(models.Model):
    image = models.ImageField(upload_to='second_top_image/')
    description = models.TextField()
    def __str__(self):
        return self.description

class MeetGuruji(models.Model):
    image = models.ImageField(upload_to='meet_guruji/')
    title = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    def __str__(self):
        return self.title

class LatestFromGuruji(models.Model):
    image = models.ImageField(upload_to='latest_from_guruji/')
    book = models.CharField(max_length=255)
    def __str__(self):
        return self.book

class AboutOtherPart(models.Model):
    heading = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='about/')
    background_image = models.ImageField(upload_to='about/')
    types_details = models.TextField()
    addon_image1 = models.ImageField(upload_to='about/', null=True, blank=True)
    addon_image2 = models.ImageField(upload_to='about/', null=True, blank=True)
    addon_image3 = models.ImageField(upload_to='about/', null=True, blank=True)

    def __str__(self):
        return self.heading