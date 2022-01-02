# In this file you'll write the html files urls paths so views.py can display them
# *******************************************************************************

from django.urls import path
from .views import UserRegisterView, UserEditView

# write paths below.
urlpatterns = [
    
    path('registration/', UserRegisterView.as_view(), name='register'),
    path('editProfile/', UserEditView.as_view(), name='editProfile')
    
]