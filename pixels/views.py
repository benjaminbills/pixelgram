from pixels.models import Profile
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import UpdateProfileForm
from .decorators import unauthenticated_user
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import  CreateUserForm



@unauthenticated_user
def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
    context = {}
    return render(request, 'registration/login.html', context)

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            Profile.objects.create(
                user=user,
            )
            messages.success(request, 'Account was creates for ' + username )
            return redirect('login')
    context = {'form':form}
    return render(request, 'registration/register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
  return render(request, 'pixels/home.html')

def profile(request, profile_id):
  profile = get_object_or_404(Profile, pk=profile_id)
  return render(request, 'profile/profile.html', {'profile':profile})

def profile_edit(request, profile_id):
  profile = get_object_or_404(Profile, pk=profile_id)
  form = UpdateProfileForm()
  print(form)
  return render(request, 'profile/profile_edit.html', {'profile':profile, 'form':form})

