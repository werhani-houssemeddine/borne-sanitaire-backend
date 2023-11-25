from lib.errors import Validator
from lib.HTTP   import HTTP_REQUEST
from lib.bcrypt import Bcrypt

from client.models import UserModel
from Repository    import UserRepository

class LoginControllerValidator:
  def __init__(self, request: HTTP_REQUEST) -> None:
    (self.email, self.password) = self.extractData(request)

  @staticmethod
  def extractData(request: HTTP_REQUEST) -> tuple[str, str]:
    email: str    = request.body.get('email').strip()
    password: str = request.body.get('password').strip()

    Validator({ 'email': email }).check_not_null('email').check_email('email')
    Validator({ 'password': password }).check_not_null('password').check_min_length('password', 10)

    return email, password
    
  def validateCredentials(self) -> UserModel | None:
    try:
      user = UserRepository.getUserByEmail(self.email)
        
      if user.email == self.email and self.__checkPassword(user.password):
        return UserModel
      return None
    
    except Exception as e:
      print(f'LoginControllerValidator.validateCredentials {e}') 
      raise
  
  def __checkPassword(self, user_password) -> bool:
    Bcrypt.rounds = 10
    return Bcrypt.compare(self.password, user_password)
        