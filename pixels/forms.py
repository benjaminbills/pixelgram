from django.forms import ModelForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        field = '__all__'
        exclude = ['user']
    
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
