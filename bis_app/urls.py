# In this file you'll write the html files urls paths so views.py can display them
# *******************************************************************************

from django.urls import path
from . import views
from .views import postView, blogView, addPosts, EditPosts, DeletePosts

urlpatterns = [

    # Home page.
    path('', views.home, name="home"),

    # Return a list of all posts
    path('bList/', postView.as_view(), name='bList'),

    # register user but bitch not working all of a sunden. 
    # path('register/', views.register, name='register'),

    # Login user.
    # path('login', views.login, name='login'),

    # Logout user.
    # path('logout', views.logout, name='logout'), 

    # Return selected post.
    path('bPosts/<int:pk>', blogView.as_view(), name='bPosts'), 

    # Add a post from a HTML page 
    path('bEditor/', addPosts.as_view(), name='bEditor'), 

    # Edit blog post
    path('bUpdate/edit/<int:pk>', EditPosts.as_view(), name='bUpdate'),

    # Edit blog post
    path('Dposts/<int:pk>/remove', DeletePosts.as_view(), name='Dposts'),
]