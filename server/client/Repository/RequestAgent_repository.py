from .User_repository import UserRepository
from client.models    import RequestAgentModel

from lib.errors import ValidationError

class RequestAgentRepository:
  @staticmethod
  def newRequestAgent(email, user_id):
    try:
      user = UserRepository.getUserById(user_id)
      requestAgent = RequestAgentModel()

      requestAgent.email   = email
      requestAgent.user_id = user
      requestAgent.save()

      return requestAgent.request_id      

    except Exception as e:
      print(e)
      raise

  @staticmethod
  def getRequestAgentByEmail(email):
    try:
      return RequestAgentModel.objects.get(email = email)
    except Exception as e:
      return None
    
  @staticmethod
  def getPendingRequestAgentById(id):
    try:
      return RequestAgentModel.objects.get(request_id = id, state = "PENDING")
    except Exception as e:
      return None
    
  @staticmethod
  def getRequestAgentById(id) -> RequestAgentModel:
    try:
      return RequestAgentModel.objects.get(request_id = id)
    
    except RequestAgentModel.DoesNotExist as ve:
      ValidationError('AGENT ID', 'FIELD NOT EXIST')
    except Exception as e:
      raise 
  
  @staticmethod
  def updateRequestAgentState(id, new_state) -> bool:
    try:
      if new_state != "PENDING" or new_state != "ACCEPT" or new_state != "REJECT":
        raise ValidationError("STATE", "INVALID STATE PROPERTY")

      request_agent = RequestAgentRepository.getRequestAgentById(id)
      request_agent.state = new_state
      request_agent.save()

      return True

    except ValidationError as e:
      raise 
    except Exception as e:
      raise
    
