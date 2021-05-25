from django.forms import ModelForm
from .models import Image, Profile
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

class NewPostForm(ModelForm):
    class Meta:
        model = Image
        exclude = ['likes', 'profile', 'user', 'post_date', 'comment']