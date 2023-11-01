from django.db import models
import uuid

class VerificationCode(models.Model):
  device_id = models.UUIDField(default = uuid.uuid4, editable = False, unique = True)
  user_id = models.ForeignKey('USER', default=None)
  version = models.CharField(max_length=8, null=False)
  is_saled = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  purchase_date = models.DateTimeField()