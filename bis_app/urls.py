# In this file you'll write the html files urls paths so views.py can display them
# *******************************************************************************

from django.urls import path
from . import views
from .views import postView, blogView, addPosts, EditPosts, DeletePosts, addCategory, CategoryView, LikesView, addComments
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    # Home page.
    path('', views.home, name="home"),

    # Return a list of all posts
    path('bList/', postView.as_view(), name='bList'),

    # Add Category 
    path('categories/', addCategory.as_view(), name='categories'),

    # show posts by category
    path('pCategories/<str:cats>/', CategoryView, name='pCategories'),

    # register user but bitch not working all of a sudden. 
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
    path('Deleteposts/<int:pk>/remove', DeletePosts.as_view(), name='Deleteposts'),

    # Likes
    path('blog_likes/<int:pk>', LikesView, name='blog_likes'),

    # comments path
    path('bPosts/<int:pk>/comments/', addComments.as_view(), name='add_comments'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)