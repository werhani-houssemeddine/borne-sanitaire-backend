import uuid

from lib.errors import Validator, ValidationError, ServerError
from lib.HTTP   import HTTP_REQUEST

from client.Repository import UserRepository, RequestAgentRepository
from client.models     import RequestAgentModel

def getUserId(request: HTTP_REQUEST) -> int:
  currentUser = request.session.get('__currentUser__')  
  if currentUser and 'id' in currentUser:
    return int(currentUser['id'])
      
  raise ServerError('USER', 'USER OR USER_ID IS MISSING IN AN AUTHORIZED ENDPOINT')


def validateUUID(uuid_str):
  try:
    return uuid.UUID(uuid_str)
  except ValueError:
    raise ValidationError('id', 'INVALID FORMAT')


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
      
      if self.checkEmailAvailability(email):
        return email.strip()

    except ValidationError: raise
    except Exception: raise 
    
    
  @staticmethod
  def checkEmailAvailability(email) -> True:
    if UserRepository.getUserByEmail(email) is None:
      return True
    raise ValidationError('email', 'EMAIL EXISTS')

  def createNewRequestAgent(self) -> str:
    try:
      request_agent_id = RequestAgentRepository.newRequestAgent(
        user_id = getUserId(self.request),
        email   = self.email
      )

      return str(request_agent_id)

    except ServerError as se:
      print(f'This error occured in AddNewRequestAgent.getUserId {e}')
      raise
    except Exception as e:
      print(f'AddNewRequestAgent.createNewRequestAgent {e}')
      raise

class RequestAgentController:
  @staticmethod
  def getSingleRequest(request: HTTP_REQUEST) -> RequestAgentModel:
    try:
      user_id    = getUserId(request)
      request_id = validateUUID(request.params.get('id'))

      if request_id is not None:      
        request_agent: RequestAgentModel = RequestAgentRepository.getRequestAgentById(request_id)
        
        if request_agent is not None:
          if request_agent.user_id.id == user_id: 
            return RequestAgentController.formatRequestAgentResponse(request_agent)
            
          raise ValidationError('UNATHORIZED', 'REQUEST ID')
        
        raise ValidationError('REQUEST', 'REQUEST NOT FOUND')
      
      raise ValidationError('REQUEST', 'REQUIRED REQUEST ID')

    except ServerError: raise
    except ValidationError: raise
    except Exception: raise

  @staticmethod
  def deleteRequestAgent(request: HTTP_REQUEST) -> bool:
    try:
      request_id = validateUUID(request.params.get('id'))
      user_id    = getUserId(request)

      if request_id is not None:
        return RequestAgentRepository.deleteRequestAgentById(user_id, request_id)

      raise ValidationError('REQUEST', 'REQUIRED REQUEST ID')
      
    except ServerError: raise
    except ValidationError: raise
    except Exception: raise
  
  @staticmethod
  def getAllRequestAgent(request: HTTP_REQUEST) -> bool:
    try:
      user_id = getUserId(request)
      listOfRequestAgent = RequestAgentRepository.getAllRequestAgent(user_id)
      return list(
        map(RequestAgentController.formatRequestAgentResponse, listOfRequestAgent)
      )
    
    except Exception as e:
      raise

  @staticmethod
  def formatRequestAgentResponse(agent: RequestAgentModel) -> dict:
    return {
      'id'         : agent.request_id,
      'agent_email': agent.email,
      'accepted'   : agent.state == "ACCEPT",
      'rejected'   : agent.state == "REJECT",
      'created_at' : agent.created_at,
    }
