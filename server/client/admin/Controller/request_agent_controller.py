from lib.errors import Validator, ValidationError, ServerError
from lib.HTTP   import HTTP_REQUEST

from client.Repository import UserRepository, RequestAgentRepository

class AddNewRequestAgentController:
  def __init__(self, request: HTTP_REQUEST) -> None:
    try:
      self.request: HTTP_REQUEST = request
      self.email  : str = self.validateEmail()
    except Exception as e:
      raise

  def getRequestId(self) -> str:
    return self.createNewRequestAgent()

  def validateEmail(self) -> str:
    try:
      email: str = self.request.body.get('email')
      Validator({ 'email': email }).check_not_null('email').check_not_empty('email').check_email('email')
      
      if self.checkEmailDisponibility(email):
        return email.strip()

    except ValidationError as ve:
      raise
    except Exception as e:
      raise 
    
  def getUserId(self) -> int:
    currentUser = self.request.session.get('__currentUser__')
    
    if currentUser != None:
      user_id = currentUser['id']
      if user_id != None:
        return int(user_id)
      
    raise ServerError('USER', 'USER OR USER_ID IS MISSING IN AN AUTHORIZED ENDPOINT')
    
  @staticmethod
  def checkEmailDisponibility(email) -> True:
    if UserRepository.getUserByEmail(email) == None:
      return True
    raise ValidationError('email', 'EMAIL EXISTS')

  def createNewRequestAgent(self) -> str:
    try:
      request_agent_id = RequestAgentRepository.newRequestAgent(
        user_id = self.getUserId(),
        email   = self.email
      )

      return str(request_agent_id)

    except ServerError as se:
      print(f'This error occured in AddNewRequestAgent.getUserId {e}')
      raise
    except Exception as e:
      print(f'AddNewRequestAgent.createNewRequestAgent {e}')
      raise