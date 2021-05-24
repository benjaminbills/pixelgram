from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class UpdateProfileForm(forms.Form):
    class Meta:
        model = Profile
        field = '__all__'
        exclude = ['username']
    
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
