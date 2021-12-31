# In this file you'll write the code so views.py can display them
# *******************************************************************************

from django.shortcuts import render, redirect, get_list_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import features, post, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# uncomment EditForm to make it work.
from .forms import PostForm # ,EditForm 
from django.urls import reverse_lazy, reverse


# Create your views here.

def home(request):
    
    multipleFeatures = features.objects.all()
    
    return render(request, 'home.html', {'features': multipleFeatures})

# get user data & error messages
def register(request):   
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already in use')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
                
        else:
            messages.info(request, 'password don\'t match')
            return redirect ('register')
    else:
        return render(request, 'register.html')

# login the user but if the password is different show an error message
# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = auth.authenticate(username=username, password=password)

#         if user is not None:
#             auth.login(request,user)
#             return redirect('/')
#         else:
#             messages.info(request, 'Invalid Credentials')
#             return redirect ('login')
#     else:
#         return render(request, 'login.html')

# log out user
def logout(request):
    auth.logout(request)
    return redirect('/')

# return posts by category
def CategoryView(request, cats):
    category_posts = post.objects.filter(category=cats)
    return render(request, 'pCategories.html', {'cats': cats.title(), 'category_posts':category_posts})


# show a list of all posts
class postView(ListView):
    model = post
    template_name = "bList.html"
    cats = Category.objects.all()


    def get_context_data(self, *args, **kwargs ):
        cat_menu = Category.objects.all()
        context = super(postView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

# Return selected post.
class blogView(DetailView ):
    model = post
    template_name = "bPosts.html"

# Add a post from a HTML page 
class addPosts(CreateView):
    model = post
    form_class = PostForm
    template_name = "bEditor.html"
    # fields = '__all__'

# add a Category
class addCategory(CreateView):
    model = Category
    # form_class = PostForm
    template_name = "categories.html"
    fields = '__all__'

# Edit Posts
class EditPosts(UpdateView):
    model = post
    # change Postform to EditForm to make it work 
    form_class = PostForm
    template_name = "bUpdate.html"
    # fields = '__all__'

class DeletePosts(DeleteView):
    model = post
    template_name = "Dposts.html"
    success_url = reverse_lazy('bList')

# Posts Likes
def LikesView(request, pk):
    Post = get_list_or_404(post, id=request.POST.get('post_id'))
    Post.likes.add(request.user)
    return HttpResponseRedirect(reverse('bPosts', args=[str(pk)]))






