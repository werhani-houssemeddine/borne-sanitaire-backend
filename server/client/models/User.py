from django.db import models

class User(models.Model):

  ROLE_CHOICES = [
    ('admin', 'ADMIN'),
    ('agent', 'AGENT')
  ]

  id = models.AutoField( primary_key = True )

  email = models.CharField(
    max_length  = 30,
    unique      = True,
    null        = False
  )

  password = models.CharField(
    max_length = 255,
    null       = False
  )

  user_name = models.CharField(
    max_length = 30,
    null       = False
  )

  role = models.CharField(
    max_length = 10,
    choices    = ROLE_CHOICES,
    null       = False
  )

  # user_id = models.ForeignKey('self', on_delete= models.CASCADE, default = None, null=True)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True) 
  