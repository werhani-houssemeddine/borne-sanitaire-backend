from client.utils.get_user_id import getUserId

from lib.bcrypt import Bcrypt 
from lib.HTTP   import HTTP_REQUEST, RESPONSE_SAMPLE
from lib.errors import ValidationError

from client.Repository import UserRepository

class OTPController:
  @staticmethod
  def enable_disable_OTP(request: HTTP_REQUEST, is_enabled) -> RESPONSE_SAMPLE:
    password = request.body.get('password')
    
    if password != None:
      user_id = getUserId(request)
      user    = UserRepository.getUserById(user_id)
      
      same_password = Bcrypt.compare(password, user.password)
      if same_password == True:
        user.otp_enabled = is_enabled
        user.save()

        return True

      raise ValidationError(field = 'password', message = 'wrong password')
    
    raise ValidationError(field = 'password', message = 'missing password')
  
  
  @staticmethod
  def checkOTP(request: HTTP_REQUEST) -> RESPONSE_SAMPLE:
    try:
      user_id = getUserId(request)
      user    = UserRepository.getUserById(user_id)

      return user.otp_enabled

    except Exception:
      raise
