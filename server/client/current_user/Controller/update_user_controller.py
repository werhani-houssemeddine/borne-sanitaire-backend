from lib.errors import ValidationError
from lib.HTTP   import HTTP_REQUEST
from lib.bcrypt import Bcrypt

from client.Repository import UserRepository

from . import UserController

class ValidateUserData:
  @staticmethod
  def validatePassword(password: str) -> bool:    
    return password != None and len(password.strip()) >= 8
  
  @staticmethod
  def comparePassword(password: str, confirm_password: str) -> bool:
    return password == confirm_password
  
  @staticmethod
  def validatePhoneNumber(number: str) -> bool:
    return number != None and number.isdigit() and len(number) == 8
  
  @staticmethod
  def validateUsername(username: str) -> bool:
    return username != None and len(username) >= 4
  

class UpdateUserController(UserController):
  def __init__(self, request: HTTP_REQUEST) -> None:
    super().__init__(request)
    self.user_id = self.current_user.id

  def updateUsername(self):
    try:
      new_username = self.extractData('username')
      if not ValidateUserData.validateUsername(new_username):
        raise ValidationError('username', 'Invalid Username')

      return UserRepository.updateUser(self.user_id, 'user_name', new_username)
    
    except ValidationError: raise 
    except Exception: raise

    
  def updatePhoneNumber(self):
    try:
      phone_number = self.extractData('phone_number')
      if not ValidateUserData.validatePhoneNumber(phone_number):
        raise ValidationError('phone_number', 'Invalid format')
    
      return UserRepository.updateUser(self.user_id, 'phone_number', phone_number)

    except ValidationError: raise
    except Exception: raise

  def updatePassword(self):
    try:
      confirm_password = self.extractData('confirm_password')
      new_password     = self.extractData('new_password')
      current          = self.extractData('current')
      
      if not ValidateUserData.validatePassword(new_password):
        raise ValidationError('new_password', 'Invalid format')
      
      if not ValidateUserData.validatePassword(confirm_password):
        raise ValidationError('confirm_password', 'Invalid format')
      
      if not ValidateUserData.comparePassword(new_password, confirm_password):
        raise ValidationError('confirm_password', 'passwords not much')

      #? Get User Password 
      user_password = UserRepository.getUserById(self.user_id).password
      
      if Bcrypt.compare(current, user_password):

        #? Hash the new password, the returned value is of type bytes
        hashedPassword = Bcrypt.hash(new_password).decode('utf-8')

        #? Save the new password
        return UserRepository.updateUser(self.user_id, 'password', hashedPassword)

      raise ValidationError('UNATHORIZED', 'Wrong password')

    except ValidationError: raise
    except Exception: raise
      

  def extractData(self, attribute: str) -> str | None:
    return self.request.body.get(attribute)
  
  