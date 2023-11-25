from lib.bcrypt import Bcrypt

from .business_rules import SingUp as SignUpValidate
from client.Repository            import UserRepository

class SignUpController:
  @staticmethod
  def validateUserData(data) -> tuple:
    try:
      return SignUpValidate.validateUserData(data)
    except Exception:
      raise

  
  @staticmethod
  def createUser(email, password, user_name, role, user = None):
    try:
      # Specify number of rounds for bcrypt hash method
      # ans hash the password
      Bcrypt.rounds   = 10
      hashed_passowrd = Bcrypt.hash(password)
      hashed_passowrd = hashed_passowrd.decode('utf-8') # Convert from byte to string

      # Cheking the user role
      if role == "ADMIN":
        return User.createNewAdmin(email = email, password = hashed_passowrd, user_name = user_name)
      
      elif role == "AGENT":
        createdAgent = User.createNewAgent(email = email, password = hashed_passowrd, user_name = user_name)
        createdAgent.user_id = user
        createdAgent.save()
        return createdAgent

    except Exception as e:
      raise