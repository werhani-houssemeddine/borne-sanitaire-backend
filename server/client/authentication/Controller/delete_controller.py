from lib.HTTP   import HTTP_REQUEST, RESPONSE_SAMPLE
from lib.errors import ValidationError
from lib.bcrypt import Bcrypt

from client.Repository import UserRepository, UserPictureRepository, AgentRepository
from client.utils      import getUserId

def DeleteAccountController(request: HTTP_REQUEST) -> RESPONSE_SAMPLE:
  password = request.body.get('password')
  try:
    if password != None:
      user_id = getUserId(request)
      user    = UserRepository.getUserById(user_id)
      
      same_password = Bcrypt.compare(password, user.password)
      if same_password == True:

        #? Delete User Picture
        UserPictureRepository.deletePictureByUserId(user_id)

        #? If the user is admin delete it's agents
        if user.role == "ADMIN":
          AgentRepository.deleteAgentsByUserId(user_id)
        
        #? Delete User
        UserRepository.deleteUserById(user_id)
        

        return True

      raise ValidationError(field= 'password', message='wrong password')
    else: 
      raise ValidationError(field = 'password', message = 'missing password')
  
  except ValidationError: raise
  except Exception: raise