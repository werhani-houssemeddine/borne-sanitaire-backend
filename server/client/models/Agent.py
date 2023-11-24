from django.db import models

class Agent(models.Model):
  
  id = models.AutoField( primary_key = True )
  susspend = models.BooleanField(default = False)
  user_id = models.ForeignKey('User' , on_delete= models.CASCADE, default = None, null=True)
  

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True) 
  