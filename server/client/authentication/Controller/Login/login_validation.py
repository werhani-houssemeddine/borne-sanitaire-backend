from lib.errors import Validator, ValidationError
from lib.HTTP   import HTTP_REQUEST
from lib.bcrypt import Bcrypt

from client.models import UserModel
from client.Repository    import UserRepository

class LoginControllerValidator:
  def __init__(self, request: HTTP_REQUEST) -> None:
    (self.email, self.password) = self.extractData(request)

  @staticmethod
  def extractData(request: HTTP_REQUEST) -> tuple[str, str]:
    email: str    = request.body.get('email')
    password: str = request.body.get('password')

    v = lambda field: \
      lambda value: Validator({ field: value }).check_not_null(field).check_not_empty(field)

    v('email')(email).check_email('email')
    v('password')(password).check_min_length('password', 10)

    return email, password
    
  def validateCredentials(self) -> UserModel | None:
    try:
      user = UserRepository.getUserByEmail(self.email)
      if user == None:
        return None
      
      if user.email == self.email and self.__checkPassword(user.password):
        return UserModel
      
      return None
    
    except ValidationError as e:
      return None
    
    except Exception as e:
      print(f'LoginControllerValidator.validateCredentials {e}') 
      raise
  
  def __checkPassword(self, user_password) -> bool:
    Bcrypt.rounds = 10
    return Bcrypt.compare(self.password, user_password)
        