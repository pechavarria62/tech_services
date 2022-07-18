# In this file you'll write the class with the fields you want to be the admin
# page remember to got to the Admin file and import the class name you made.
# *******************************************************************************
from distutils.command.upload import upload
from turtle import ondrag
from django.db import models
from django.db.models.fields import CharField
from datetime import datetime, date
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here
class features(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    price = models.CharField(max_length=30)
    details_na = models.CharField(max_length=100)

# create categories
class Category(models.Model):
    name = models.CharField(max_length=100)
    # show title
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('bList')

#make a one to one field 
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return str(self.user)


# make blog posts
class post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    category = models.CharField(max_length=200, default="")
    snippet = models.CharField(max_length=200,)
    likes = models.ManyToManyField(User, related_name='blog_likes')

    def total_likes(self):
        return self.likes.count()

    # show title
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('bList')

