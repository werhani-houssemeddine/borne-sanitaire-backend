from lib.bcrypt import Bcrypt
from lib.token  import Token
from lib.Http   import HTTP_REQUEST, RESPONSE_SAMPLE

from client.authentication.Signup.business_rules import SingUp as SignUpValidate
from client.authentication.Repository            import User

class SignUpController:
  
  @staticmethod
  def singup(request: HTTP_REQUEST):
    try:
      # this function either return a tuple (email, password, user_name, role)
      # or throw a new error
      (email, password, user_name, role) = SignUpValidate.validateUserData(request.body)

      # Get User by looking user_email
      is_user_exist = User.getUserByEmail(email)

      # Check user existing
      if is_user_exist != None:
        return RESPONSE_SAMPLE.badRequest({ 'email': 'PROPERTY VALUE ALREADY EXIST' })
      
      # Specify number of rounds for bcrypt hash method
      # ans hash the password
      Bcrypt.rounds   = 10
      hashed_passowrd = Bcrypt.hash(password)
      hashed_passowrd = hashed_passowrd.decode('utf-8') # Convert from byte to string


      user = None # It will have the new user data

      # Save new user
      #! We must add device id for admins
      #! and agence_id for Agents
      if role == "ADMIN":
        user = User.createNewAdmin(email = email, password = hashed_passowrd, user_name = user_name)
      
      elif role == "AGENT":
        user = User.createNewAgent(email = email, password = hashed_passowrd, user_name = user_name)

      # generate Token
      payload = { 'email': user.email, 'id': user.id }
      jwt_token = Token.createToken(payload)

      return writeCredentials(token = jwt_token)

    except Exception as e:
      print(e)
      return RESPONSE_SAMPLE.badRequest({ 'details': str(e) })
      
  

def writeCredentials(token: str) -> dict:
  return {
    'status_code': 201,
      'body'       : {
        'message': 'CREATED SUCCESSFULLY',
        'state'  : 'success',
        'error'  : False,
        'data': {
          'token': token,
        }
      }
  }