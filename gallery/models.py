from django.db import models

# Create your models here.
class Add_Photo(models.Model):
    photo=models.ImageField(upload_to='photos/')
    def __str__(self):
        return self.photo
class Add_video(models.Model):
    video=models.ImageField(upload_to='videos/')
    video_link=models.URLField()
    def __str__(self):
        return self.video