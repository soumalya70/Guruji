from django.db import models

class Blog(models.Model):
    title= models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    image=models.ImageField(upload_to='blog/',default='input image')
    title1=models.CharField(max_length=100,default='Type Here')
    long_description1 = models.TextField(default='Type Here')
    title2=models.CharField(max_length=100,blank=True,default='Type Here')
    long_description2 = models.TextField(blank=True,default='Type Here')
    def __str__(self):
        return self.title


# class Nature(models.Model):
#     title= models.CharField(max_length=100)
#     description = models.TextField(max_length=200)
#     image=models.ImageField(upload_to='blog/',default='input image')
#     title1=models.CharField(max_length=100,default='Type Here')
#     long_description1 = models.TextField(default='Type Here')
#     title2=models.CharField(max_length=100,blank=True,default='Type Here')
#     long_description2 = models.TextField(blank=True,default='Type Here')
#     def __str__(self):
#         return self.title
# class Political(models.Model):
#     title= models.CharField(max_length=100)
#     description = models.TextField(max_length=200)
#     image=models.ImageField(upload_to='blog/',default='input image')
#     title1=models.CharField(max_length=100,default='Type Here')
#     long_description1 = models.TextField(default='Type Here')
#     title2=models.CharField(max_length=100,blank=True,default='Type Here')
#     long_description2 = models.TextField(blank=True,default='Type Here')
#     def __str__(self):
#         return self.title
    
# class Sports(models.Model):
#     title= models.CharField(max_length=100)
#     description = models.TextField(max_length=200)
#     image=models.ImageField(upload_to='blog/',default='input image')
#     title1=models.CharField(max_length=100,default='Type Here')
#     long_description1 = models.TextField(default='Type Here')
#     title2=models.CharField(max_length=100,blank=True,default='Type Here')
#     long_description2 = models.TextField(blank=True,default='Type Here')
#     def __str__(self):
#         return self.title

# class Social(models.Model):
#     title= models.CharField(max_length=100)
#     description = models.TextField(max_length=200)
#     image=models.ImageField(upload_to='blog/',default='input image')
#     title1=models.CharField(max_length=100,default='Type Here')
#     long_description1 = models.TextField(default='Type Here')
#     title2=models.CharField(max_length=100,blank=True,default='Type Here')
#     long_description2 = models.TextField(blank=True,default='Type Here')
    
#     def __str__(self):
#         return self.title
    
# class Religious(models.Model):
#     title= models.CharField(max_length=100)
#     description = models.TextField(max_length=200)
#     image=models.ImageField(upload_to='blog/',default='input image')
#     title1=models.CharField(max_length=100,default='Type Here')
#     long_description1 = models.TextField(default='Type Here')
#     title2=models.CharField(max_length=100,blank=True,default='Type Here')
#     long_description2 = models.TextField(blank=True,default='Type Here')

#     def __str__(self):
#         return self.title