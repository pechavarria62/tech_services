# In this file you'll write the class to style the post editor fields
# *******************************************************************************

# make imports 
from django import forms
from .models import post, Category

# Add Category choices hard coded
# choices = [('Sports','Sports'),('No Category','No Category'),('Food','Food'),('Veganism','Veganism')]

# Add Category choices but dynamically 
choices = Category.objects.all().values_list('name','name')

choice_list= []

# Loop trough choices
for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ('title', 'author', 'category', 'body', 'created_at')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'author'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
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

