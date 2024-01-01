from client.utils.get_user_id import getUserId

from lib.bcrypt import Bcrypt 
from lib.HTTP   import HTTP_REQUEST, RESPONSE_SAMPLE
from lib.errors import ValidationError, Validator

from client.Repository import UserRepository, OTP_Repository

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

  @staticmethod
  def compareOTP(request: HTTP_REQUEST):
    try:
      email  = request.body.get('email')
      v_code = request.body.get('verification_code')

      Validator({ 'email': email, 'verification code': v_code }) \
        .check_email('email').check_not_null('verification code') \
        .check_not_empty('verification code')
      print(email, int(v_code))
      if OTP_Repository.compareOTP(email, int(v_code)):
        
        OTP_Repository.deleteOTP(email)
        return True
      
      raise ValidationError('verification code', 'expired verification code')

    except Exception as e:
      print(e)
      raise
      
  @staticmethod
  def generateOTP(email: str):
    return OTP_Repository.createNewOTP(email)