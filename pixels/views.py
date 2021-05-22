from pixels.models import Profile
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

def home(request):
  return render(request, 'pixels/home.html')

def profile(request, profile_id):
  profile = get_object_or_404(Profile, pk=profile_id)
  return render(request, 'profile/profile.html', {'profile':profile})
