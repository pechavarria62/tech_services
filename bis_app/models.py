# In this file you'll write the class with the fileds you want to be the admin
# page remember to got to the Admin file and impot the class name you made.
# *******************************************************************************
from django.db import models
from django.db.models.fields import CharField
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here
class features(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    price = models.CharField(max_length=30)
    datails_na = models.CharField(max_length=100)

# create categories
class Category(models.Model):
    name = models.CharField(max_length=100)
    # show title
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('bList')


# make blog posts
class post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    category = models.CharField(max_length=200, default="")
    likes = models.ManyToManyField(User, related_name='blog_likes')

    def total_likes(self):
        return self.likes.count()

    # show title
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('bList')

