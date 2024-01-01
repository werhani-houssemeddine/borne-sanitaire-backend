from django.db import models

from administration.models import Device
from .User import User

class AgentPermessionsModel(models.Model):  
  #? Agent Id will reference to the agent from user table 
  agent_id: User = models.ForeignKey('User', on_delete= models.CASCADE)
  
  device_id = models.ForeignKey ('administration.Device', on_delete= models.CASCADE)

  check_historic = models.BooleanField(default = False)
  config_device  = models.BooleanField(default = False)
  
  