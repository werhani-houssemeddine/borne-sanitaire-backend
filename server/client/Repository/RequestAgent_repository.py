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
      if new_state != "PENDING" and new_state != "ACCEPT" and new_state != "REJECT":
        raise ValidationError("STATE", "INVALID STATE PROPERTY")

      request_agent = RequestAgentRepository.getRequestAgentById(id)
      request_agent.state = new_state
      request_agent.save()

      return True

    except ValidationError as e:
      raise 
    except Exception as e:
      raise


  @staticmethod
  def getAllRequestAgent(user_id: int):
    try:
      return RequestAgentModel.objects.filter(user_id = user_id, state = "PENDING")
    except RequestAgentModel.DoesNotExist:
      return None
    except Exception:
      raise 

  @staticmethod
  def deleteRequestAgentById(user_id: int, request_id) -> True:
    try:
      RequestAgentModel.objects.get(user_id = user_id, request_id = request_id).delete()
      return True
    except RequestAgentModel.DoesNotExist:
      raise ValidationError('REQUEST', 'REQUEST NO MORE VALID')
    except Exception:
      raise
