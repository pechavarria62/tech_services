from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db.models import fields
from bis_app.models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

# here will be a list of the field to update un the settings page.
class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_login = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_joined = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_active = forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    

    class Meta:
        model = User
        fields = ('email','username', 'first_name', 'last_name', 'password', 'last_login', 'date_joined', 'is_active')


class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'website_url', 'facebook_url', 'instagram_url', 'github_url'  )
        widgets = {

            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            # 'profile_pic': forms.TextInput(attrs={'class': 'form-control', 'id': 'author'}),
            'website_url': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
            'github_url': forms.TextInput(attrs={'class': 'form-control'}),

        }
