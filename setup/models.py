from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE, default=1)
  title = models.TextField(max_length=1000)
  blog = models.TextField(max_length=20000)
  image = models.ImageField(upload_to='static/image/', null = True, blank= True)

  created_date = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return self.user.username

# class UserProfile(models.Model):
