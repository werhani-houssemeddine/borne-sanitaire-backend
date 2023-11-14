from django.db import models
from django.core.validators import RegexValidator

class SuperAdmin(models.Model):
  phone_number = models.CharField(max_length=8, validators=[RegexValidator(r'^[0-9]{8}$', 'Phone number must be 8 digits')])
  username     = models.CharField(max_length=255)
  password     = models.CharField(max_length=255)  
  email        = models.EmailField()

  created_at = models.DateTimeField(auto_now_add=True)