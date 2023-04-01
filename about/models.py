from django.db import models

# Create your models here.
from django.db import models

class Guruji(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='about/')
    guruji_image = models.ImageField(upload_to='guruji_images/')
    meet_guruji_image = models.ImageField(upload_to='meet_guruji/')
    book_image = models.ImageField(upload_to='book_images/')
    def __str__(self):
        return self.description
    
class Horoscope(models.Model):
    title=models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='second_top_image/')
    title1=models.CharField(max_length=100)
    description1=models.TextField()
    title2=models.CharField(max_length=100)
    description2=models.TextField()
    title3=models.CharField(max_length=100)
    description3=models.TextField()
    title4=models.CharField(max_length=100)
    description4=models.TextField()
    def __str__(self):
        return self.title

class Kundli(models.Model):
    title=models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='second_top_image/')
    title1=models.CharField(max_length=100)
    description1=models.TextField()
    title2=models.CharField(max_length=100)
    description2=models.TextField()
    title3=models.CharField(max_length=100)
    description3=models.TextField()
    title4=models.CharField(max_length=100)
    description4=models.TextField()
    def __str__(self):
        return self.title

class Gorchar(models.Model):
    title=models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='second_top_image/')
    title1=models.CharField(max_length=100)
    description1=models.TextField()
    title2=models.CharField(max_length=100)
    description2=models.TextField()
    title3=models.CharField(max_length=100)
    description3=models.TextField()
    title4=models.CharField(max_length=100)
    description4=models.TextField()
    def __str__(self):
        return self.title

class Vedic_astrology(models.Model):
    title=models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='second_top_image/')
    title1=models.CharField(max_length=100)
    description1=models.TextField()
    title2=models.CharField(max_length=100)
    description2=models.TextField()
    title3=models.CharField(max_length=100)
    description3=models.TextField()
    title4=models.CharField(max_length=100)
    description4=models.TextField()
    def __str__(self):
        return self.title

# class AboutOtherPart(models.Model):
#     heading = models.CharField(max_length=100)
#     description = models.TextField()
#     image = models.ImageField(upload_to='about/')
#     background_image = models.ImageField(upload_to='about/')
#     types_details = models.TextField()
#     addon_image1 = models.ImageField(upload_to='about/', null=True, blank=True)
#     addon_image2 = models.ImageField(upload_to='about/', null=True, blank=True)
#     addon_image3 = models.ImageField(upload_to='about/', null=True, blank=True)

#     def __str__(self):
#         return self.heading