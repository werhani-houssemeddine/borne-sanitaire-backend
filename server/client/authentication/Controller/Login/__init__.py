from lib.Http.http_request import HTTP_REQUEST
from lib.bcrypt            import Bcrypt 
from lib.token             import Token

from .business_rules import LogIn as LoginValidate
from client.Repository import User
from client.models     import User as UserTable 
class LoginController:
  
  @staticmethod
  def chekUserData(request: HTTP_REQUEST) -> tuple:
    try:
      # this function either return a tuple (email, password)
      # or throw a new error
      (email, password) = LoginValidate.validateUserData(request.body)
      return (email, password)
    
    except Exception as e:
      raise e     
    
  @staticmethod
  def checkCredentialse(email, password) -> UserTable | None:
    try:
      # Return User by looking user_email
      user = User.getUserByEmail(email)
      
      # User not found
      if user == None:
        return None

      # Specify number of rounds for bcrypt hash method
      Bcrypt.rounds = 10

      # Comparing password
      if Bcrypt.compare(password, user.password) == False:
        return None
      return user
      
    except Exception as e:
      raise e
  
  @staticmethod
  def generateToken(user: UserTable):
    payload = { 'email': user.email, 'id': user.id, 'username': user.user_name, 'role': user.role }
    return Token.createToken(payload)
  
  @staticmethod 
  def generateResponse(user: UserTable, token: str) -> dict:
    return {
      'username': user.user_name,
      'isAdmin' : user.role == "ADMIN",
      'isAgent' : user.role == "AGENT",
      'token'   : token
    }