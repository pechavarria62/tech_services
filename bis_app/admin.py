# this file output the fields used in the admin page
# **********************************************************

# Here import  the classes you made in the Models file using 
#(from .models import ) and the name of the class.
from django.contrib import admin
from .models import features, post

# Register your models here to be shown in the admin page
# use (admin.site.register(name of class))
admin.site.register(features)
admin.site.register(post)