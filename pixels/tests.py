from django.contrib.auth.models import User
from django.test import TestCase
from .models import Comment, Profile, Image
# Create your tests here.

class ProfileTestClass(TestCase):
  def setUp(self):
      self.user = User(username='Benjamin', email='ben@gmail.com', password='Bananna')
      self.user.save()
      self.profile = Profile(profile_photo='http:cloudinary/PixelGram/profile/ben.jpg', bio='I am amazing', user=self.user)
      
      # Testing  instance
  def test_instance(self):
      self.assertTrue(isinstance(self.profile,Profile))  
  def test_save_method(self):
      self.profile.save_profile()     
      profile = Profile.objects.all()
      self.assertTrue(len(profile) > 0) 
  def tearDown(self):
      Profile.objects.all().delete()
  def delete_profile(self):
      self.profile.save_profile()
      profile=Profile.objects.all()
      self.assertEqual(len(profile), 1) 
      self.profile.delete_profile()
      del_profile=Profile.objects.all()
      self.assertEqual(len(del_profile),0)

  def test_update_profile(self):
      self.profile.save_profile()
      self.profile.update_profile(self.profile.id, bio='I am good', profile_photo='http:image2')
      update_bio=Profile.objects.get(bio='I am good')
      update_profile_photo=Profile.objects.get(profile_photo='http:image2')
      self.assertEqual(update_bio.bio,'I am good') 
      self.assertEqual(update_profile_photo.profile_photo,'http:image2') 


class ImageTestClass(TestCase):
  def setUp(self):
      self.user = User(username='Benjamin', email='ben@gmail.com', password='Bananna')
      self.user.save()
      self.image = Image(image='http:cloudinary/PixelGram/profile/ben.jpg', image_name='peace', user=self.user, image_caption='wake up')
      
      # Testing  instance
  def test_instance(self):
      self.assertTrue(isinstance(self.image,Image))

  def test_save_method(self):
      self.image.save_image()     
      image = Image.objects.all()
      self.assertTrue(len(image) > 0) 
  def tearDown(self):
      Image.objects.all().delete()
  def delete_image(self):
      self.image.save_image()
      image=Image.objects.all()
      self.assertEqual(len(image), 1) 
      self.image.delete_image()
      del_image=image.objects.all()
      self.assertEqual(len(del_image),0)
  def test_update_image(self):
      self.image.save_image()
      self.image.update_image(self.image.id, image_name='good', image='http:image2')
      update_name=Image.objects.get(image_name='good')
      update_image=Image.objects.get(image='http:image2')
      self.assertEqual(update_name.image_name,'good') 
      self.assertEqual(update_image.image,'http:image2') 

class CommentTestClass(TestCase):
  def setUp(self):
      self.user = User(username='Benjamin', email='ben@gmail.com', password='Bananna')
      self.user.save()
      self.image = Image(image='http:cloudinary/PixelGram/profile/ben.jpg', image_name='peace', user=self.user, image_caption='wake up')
      self.image.save()
      self.comment = Comment(comment = 'Amazing!!', user = self.user, image = self.image)
      # Testing  instance
  def test_instance(self):
      self.assertTrue(isinstance(self.comment,Comment))

  def test_save_method(self):
      self.comment.save_comment()     
      comment = Comment.objects.all()
      self.assertTrue(len(comment) > 0) 

  def tearDown(self):
      Comment.objects.all().delete()
  def delete_comment(self):
      self.comment.save_comment()
      comment=Comment.objects.all()
      self.assertEqual(len(comment), 1) 
      self.comment.delete_comment()
      del_comment=Comment.objects.all()
      self.assertEqual(len(del_comment),0)
  
  def test_update_comment(self):
      self.comment.save_comment()
      self.comment.update_comment(self.comment.id, comment='good job')
      update_comment=Comment.objects.get(comment='good job')
      
      self.assertEqual(update_comment.comment,'good job')  