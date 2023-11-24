from django.db import models

class Agent(models.Model):

  id = models.AutoField( primary_key = True )
  susspend = models.BooleanField(default = False)
  
  #? User Id will reference to the admin
  user_id = models.ForeignKey('User' , on_delete= models.CASCADE, related_name = "agent_user_id")

  #? Agent Id will reference to the agent from user table 
  agent_id = models.ForeignKey('User', on_delete= models.CASCADE, related_name = "agent_agent_id")

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True) 
  