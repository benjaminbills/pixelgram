from pixels.models import Image, Profile
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from django.forms import inlineformset_factory
from .decorators import unauthenticated_user
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import  CreateUserForm, NewPostForm



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

@login_required(login_url='login')
def accountSettings(request):
	profile = request.user.profile
	form = ProfileForm(instance=profile)
	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES,instance=profile)
		if form.is_valid():
			form.save()


	context = {'form':form}
	return render(request, 'profile/account_settings.html', context)

@login_required(login_url='login')
def userPage(request):
    profile = request.user.profile
    context = {'profile':profile }
    return render(request, 'profile/profile.html', context)

def profile(request, profile_id):
  profile = get_object_or_404(Profile, pk=profile_id)
  return render(request, 'profile/profile.html', {'profile':profile})

@login_required(login_url='login')
def createPost(request, pk):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('index')

    else:
        form = NewPostForm()
        context = {'form':form}
    return render(request, 'post/post.html', context)