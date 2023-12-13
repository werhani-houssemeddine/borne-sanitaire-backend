# This model will have the list of requested agent 

from django.db import models
from .User     import User 

class NotificationPreferencesModel(models.Model):

  user_id = models.ForeignKey(User, on_delete= models.CASCADE)

  agent_suspend_account = models.BooleanField(default = False)
  device_configuration_change = models.BooleanField(default = False)
  request_agent_response = models.BooleanField(default = False)

  reached_max_visitors = models.BooleanField(default = True)
  hight_max_visitors = models.BooleanField(default = True)

