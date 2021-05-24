from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
  profile_photo=models.ImageField(upload_to='profile_photos/', blank=True)
  bio=models.CharField(max_length=1000, default='DEFAULT VALUE')
  username=models.ForeignKey(User, on_delete=models.CASCADE)

class Image(models.Model):
  image=models.ImageField(upload_to='post/', blank=True)
  image_name=models.CharField(max_length=100)
  likes = models.IntegerField()
  comment = models.CharField(max_length=255)
