from django.db import models

class Astrology(models.Model):
    title= models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Nature(models.Model):
    title= models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
class Political(models.Model):
    title= models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title
    
class Sports(models.Model):
    title= models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Social(models.Model):
    title= models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
class Religious(models.Model):
    title= models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title