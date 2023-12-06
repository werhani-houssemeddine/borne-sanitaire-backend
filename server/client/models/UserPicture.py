from django.db import models

from . import User

class UserPicture(models.Model):
  user_id: User = models.ForeignKey('User' , on_delete= models.CASCADE)
  avatar        = models.ImageField(upload_to='uploads/')

def __str__(self):
  return self.title