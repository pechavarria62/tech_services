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

class post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    # show title
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('bList')

