from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm

# Create your views here.

# User registration form
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')


# Edit user info.
class UserEditView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'editProfile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user