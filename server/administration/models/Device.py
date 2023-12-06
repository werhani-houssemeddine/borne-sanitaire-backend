from django.db import models
import uuid

from client.models import UserModel

class Device(models.Model):
  device_id = models.UUIDField(default = uuid.uuid4, editable = False, unique = True)
  user_id = models.ForeignKey(UserModel, default=None, on_delete= models.SET_NULL, null=True)
  version = models.CharField(max_length=8, null=False)
  is_saled = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  purchase_date = models.DateTimeField(null=True)
  max_visitors = models.PositiveIntegerField(null=True, default = 0)
  title = models.CharField(max_length = 32, null=True)