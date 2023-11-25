from lib.errors import ValidationError
from lib.HTTP   import HTTP_REQUEST
from lib.token  import Token

from client.models import UserModel

from .login_validation import LoginControllerValidator

class LoginController:

  @staticmethod
  def validateData(request: HTTP_REQUEST) -> UserModel:
    try:
      #? This class will validate the data and the user existing 
      #? and return the user if credentials are corrects otherwise null
      #? he also will throw an error if there is one
      return LoginControllerValidator(request).validateCredentials()
      
    except ValidationError as ve:
      raise ve
    except Exception as e:
      print(f'LoginController.validateData {e}')
      raise e
    
  @staticmethod
  def generateToken(user: UserModel):
    payload = { 'email': user.email, 'id': user.id, 'username': user.user_name, 'role': user.role }
    return Token.createToken(payload)
  
  @staticmethod
  def login(user: UserModel | None) -> dict:
    try:
      if user is None:
        raise ValidationError('user', 'Invalid user')

      return {
        'username': user.user_name,
        'isAdmin' : user.role == "ADMIN",
        'isAgent' : user.role == "AGENT",
        'token'   : LoginController.generateToken(user)
      }
    except ValidationError as ve:
      raise ve
    except Exception as e:
      print(f'LoginController.login {e}') 
      raise