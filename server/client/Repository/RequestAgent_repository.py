from .User_repository import UserRepository
from client.models    import RequestAgent as RequestAgentTable


class RequestAgentRepository:
  @staticmethod
  def newRequestAgent(email, user_id):
    try:
      user = UserRepository.getUserById(user_id)
      requestAgent = RequestAgentTable()

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
      return RequestAgentTable.objects.get(email = email)
    except Exception as e:
      return None
    
  @staticmethod
  def getPendingRequestAgentById(id):
    try:
      return RequestAgentTable.objects.get(request_id = id, state = "PENDING")
    except Exception as e:
      return None
    
  @staticmethod
  def getRequestAgentById(id):
    try:
      return RequestAgentTable.objects.get(request_id = id)
    except Exception as e:
      return None