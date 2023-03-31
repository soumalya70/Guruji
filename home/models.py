from django.db import models
from django.db.models import Model
# Create your models here.

class BannerImage(models.Model):
    banner_description = models.TextField(max_length=255)
    banner_background = models.ImageField(upload_to='banners/', blank=True)
    banner_image = models.ImageField(upload_to='banners/')
    
    def __str__(self):
        return self.banner_description

class AboutGuruji(models.Model):
    image = models.ImageField(upload_to='about/')
    description = models.TextField()
    def __str__(self):
        return self.description
class Our_Services_Cards(models.Model):
    image=models.ImageField(upload_to='our_services_cards/')
    title=models.CharField(max_length=150)
    description=models.TextField()
    def __str__(self):
        return self.title
class Todays_Updates(models.Model):
    nakshatra=models.CharField(max_length=150)
    image=models.ImageField(upload_to='todays_updates/')
    tithi=models.CharField(max_length=150)
    sunrise=models.CharField(max_length=150)
    sunset=models.CharField(max_length=150)
    yoga=models.CharField(max_length=150)
    rashi=models.CharField(max_length=150)
    description=models.TextField()
    todays_update=models.TextField()
    def __str__(self):
        return self.nakshatra    
class ResolveProblem(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='resolve_problem/')
    def __str__(self):
        return self.description

class GurujiWords(models.Model):
    image = models.ImageField(upload_to='guruji_words/',blank=True)
    heading = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return self.banner_description

class Aaj_ka_Rashifal(models.Model):
    Aries=models.TextField()
    Taurus=models.TextField()
    Gemini=models.TextField()
    Cancer=models.TextField()
    Leo=models.TextField()
    Virgo=models.TextField()
    Libra=models.TextField()
    Scorpio=models.TextField()
    Sagittarius=models.TextField()
    Capricorn=models.TextField()
    Aquarius=models.TextField()
    Pisces=models.TextField()
    def __str__(self):
        return self.Aries
    
class Festival(models.Model):
    date = models.DateField()
    description = models.TextField()
    def __str__(self):
        return self.description

class Testimonial(models.Model):
    image = models.ImageField(upload_to='testimonial/')
    description = models.TextField()
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.description
    
class Appointment(models.Model):
    date=models.DateField()
    address=models.TextField(max_length=255)
    def __str__(self):
        return self.address

class Footer(models.Model):
    contact_no=models.CharField(max_length=12)
    email_id=models.EmailField()
    Address=models.TextField(max_length=255)
    facebook = models.CharField(max_length=255, default='https://www.facebook.com/my-page')
    instagram = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return self.Address
class Testimonial_status(models.Model):
    Happy_Clients=models.IntegerField()
    Services_Available=models.IntegerField()
    Happy_Family=models.IntegerField()
    def __str__(self):
        return self.Happy_Clients


