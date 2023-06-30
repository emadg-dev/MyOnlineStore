from django import forms 
from accounts import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 

class UserAddForm(UserCreationForm):
    class Meta(UserCreationForm): 
        model = models.CustomUser 
        fields = UserCreationForm.Meta.fields + ('email','city','supplier')

# class UserChangeForm(UserChangeForm):
#     class Meta: 
#         model = models.CustomUser 
#         fields = UserChangeForm.Meta.fields