from django.db import models

# Create your models here.
class Card(models.Model):
    image=models.ImageField(upload_to='images/')
    heading=models.CharField(max_length=200)
    description=models.TextField(max_length=255)
    def __str__(self):
        return self.heading
class Description(models.Model):
    text=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images/')
    description=models.TextField(max_length=255)
    def __str__(self):
        return self.text