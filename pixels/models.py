from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
  profile_photo=models.ImageField(upload_to='profile_photos/', default='profile_photos/default_nlfwhd', blank=True)
  bio=models.TextField(max_length=1000, default='DEFAULT VALUE')
  user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
  def save_profile(self):
        self.save()
  def delete_profile(self):
        self.delete()
  @classmethod
  def update_profile(cls, profile_id, bio, profile_photo):
        profile = cls.objects.filter(pk=profile_id).update(bio=bio,profile_photo=profile_photo)
        return profile
class Image(models.Model):
  image=models.ImageField(upload_to='post/', blank=True)
  image_name=models.CharField(max_length=100)
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  image_caption = models.CharField( max_length=100, default='Default')
  likes = models.ManyToManyField(User, related_name='likes', blank=True,)

  def total_likes(self):
    return self.likes.count()

  def save_image(self):
        self.save()

  def delete_image(self):
        self.delete()

  @classmethod
  def update_image(cls, id, image_name, image):
        image = cls.objects.filter(pk=id).update(image_name=image_name,image=image)
        return image
class Comment(models.Model):
    comment = models.TextField(max_length=2200)
    user = models.ForeignKey(User, related_name='commented_by', on_delete=models.CASCADE)
    image = models.ForeignKey(Image, related_name='comment_for', on_delete=models.CASCADE)
    pub_date=models.DateField(auto_now_add=True)

    def save_comment(self):
          self.save()

    def delete_comment(self):
          self.delete()

    @classmethod
    def update_comment(cls, id, comment):
          comment = cls.objects.filter(pk=id).update(comment=comment)
          return comment