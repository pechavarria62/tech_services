from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, UserChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm

# Create your views here.


# Password change page.
class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')
    # success_url = reverse_lazy('login')

# To create a password change success page I think.
def password_success(request):
    return render(request, 'registration/password_success.html', {})


# User registration form
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')


# Edit user info.
class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'editProfile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user