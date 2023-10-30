from django.db import models

class User(models.Model):

  ROLE_CHOICES = [
    ('admin', 'ADMIN'),
    ('agent', 'AGENT')
  ]

  email = models.CharField(
    primary_key = True,
    max_length  = 30,
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

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True) 
  