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
  def generateToken(user: UserModel) -> bytes:
    payload = { 'email': user.email, 'id': user.id, 'username': user.user_name, 'role': user.role }
    return Token.createToken(payload)
  