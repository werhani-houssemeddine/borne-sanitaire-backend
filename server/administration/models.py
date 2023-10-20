from django.db import models
import uuid

class VerificationCode(models.Model):
  code = models.CharField(max_length=12, null=False)
  ip = models.CharField(
    max_length = 20, 
    null       = False, 
    unique     = True
  )
  created_at = models.DateTimeField(auto_now_add=True)
  number_of_attempts = models.IntegerField(default=0)
  session_id = models.UUIDField(default = uuid.uuid4, editable = False, unique = True)