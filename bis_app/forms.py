# In this file you'll write the class to style the post editor fields
# *******************************************************************************

# make imports 
from django import forms
from .models import post

class PostForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ('title', 'author', 'body', 'created_at')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'created_at': forms.TextInput(attrs={'class': 'form-control'}),

        }

#******** If desired to have specific fields in the edit page ********

# class EditForm(forms.ModelForm):
#     class Meta:
#         model = post
#         fields = ('title', 'author', 'body', 'created_at')

#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'author': forms.Select(attrs={'class': 'form-control'}),
#             'body': forms.Textarea(attrs={'class': 'form-control'}),
#             'created_at': forms.TextInput(attrs={'class': 'form-control'}),

#         }

