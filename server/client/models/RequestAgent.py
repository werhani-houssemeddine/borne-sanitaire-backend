# This model will have the list of requested agent 

from django.db import models
from .User     import User 

class RequestAgent(models.Model):

  REQUEST_STATE = [
    ('pending', 'PENDING'),
    ('accept', 'ACCEPT'),
    ('reject', 'REJECT')
  ]

  id = models.AutoField( primary_key = True )
  
  user_id = models.ForeignKey(User, on_delete= models.CASCADE)

  email = models.CharField(
    max_length  = 30,
    unique      = True,
    null        = False
  )

  state = models.CharField(
    max_length = 10,
    choices    = REQUEST_STATE,
    null       = False,
    default    = 'PENDING' 
  )

  created_at = models.DateTimeField(auto_now_add=True)
  