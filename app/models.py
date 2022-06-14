from datetime import date
import re
from unicodedata import name
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="profile")
    profile_photo = CloudinaryField('image', default='default.png')
    bio = models.TextField(max_length=500, blank=True)
    name = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    contact = models.EmailField(max_length=255, blank=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    description = models.TextField(max_length=255)
    technologies = models.CharField(max_length=255, blank=True)
    photo = CloudinaryField('image')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    date = models.DateField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return f'{self.title}'
    
    def delete_post(self):
        self.delete()
        
    @classmethod
    def search_projects(cls, title):
        return cls.objects.filter(title__icontains=title).all()
    
    @classmethod
    def all_posts(cls):
        return cls.objects.all()
    
    def save_post(self):
        self.save()
        
    # resizing images


    # def save(self, *args, **kwargs):
    #     super().save()

    #     img = CloudinaryField.open(self.avatar.path)

    #     if img.height > 100 or img.width > 100:
    #         new_img = (100, 100)
    #         img.thumbnail(new_img)
    #         img.save(self.avatar.path)
        
        
class Rating(models.Model):
   rating =((1, '1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'),(8,'8'),(9,'9'),(10,'10'))
   design = models.IntegerField(choices=rating, blank=True)
   usability = models.IntegerField(choices=rating, blank=True)
   content = models.IntegerField(choices=rating, blank=True)
   score = models.IntegerField(default=0, blank=True)
   design_average = models.FloatField(default=0, blank=True)
   usability_average= models.FloatField(default=0, blank=True)
   content_average = models.FloatField(default=0, blank=True)
   user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rater",null=True)
   post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="ratings", null=True)
   
   def save_rating(self):
        self.save()
   
   def __str__(self):
       return f'{self.post} Rating'
   
   @classmethod
   def get_ratings(cls, id):
       ratings = Rating.objects.filter(post_id=id).all()
       return ratings

    # resizing images


    
