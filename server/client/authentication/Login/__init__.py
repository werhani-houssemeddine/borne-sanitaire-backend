from lib.Http.http_request import HTTP_REQUEST
from lib.Http              import RESPONSE_SAMPLE
from lib.bcrypt            import Bcrypt 
from lib.token             import Token

from client.authentication.Login.business_rules import LogIn as LoginValidate
from client.authentication.Repository           import User

class LoginController:
  
  @staticmethod
  def login(request: HTTP_REQUEST):
    try:
      # this function either return a tuple (email, password)
      # or throw a new error
      (email, password) = LoginValidate.validateUserData(request.body)

      # Get User by looking user_email
      user = User.getUserByEmail(email)

      # Check user existing
      if user == None:
        return wrongCredentials()
      
      # Specify number of rounds for bcrypt hash method
      # Comparing password
      Bcrypt.rounds = 10
      if Bcrypt.compare(password, user.password) == False:
        return wrongCredentials()
        
      # generate Token
      payload = { 'email': email, 'id': user.id, 'username': user.user_name }
      jwt_token = Token.createToken(payload)

      return writeCredentials(token = jwt_token)

    except Exception as e:
      RESPONSE_SAMPLE.badRequest({ 'details': str(e) })
  



def wrongCredentials():
  return {
    'status_code': 401,
      'body'       : {
        'message': 'WRONG CREDENTIALS',
        'state'  : 'failure',
        'error'  : False,
      }
  }

def writeCredentials(token: str) -> dict:
  return {
    'status_code': 200,
      'body'       : {
        'message': 'LOGIN SUCCESSFULLY',
        'state'  : 'success',
        'error'  : False,
        'data': {
          'token': token
        }
      }
  }