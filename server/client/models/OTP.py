# This model will have the list of requested agent 

from django.db import models
from .User     import User 


class OTP_Model(models.Model):

  email = models.CharField(max_length=32, null=False)
  code  = models.IntegerField()

  created_at = models.DateTimeField(auto_now_add=True)
  