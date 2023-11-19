from .User_repository import User
from client.models    import RequestAgent as RequestAgentTable


class RequestAgent:
  @staticmethod
  def newRequestAgent(email, user_id):
    try:
      user = User.getUserById(user_id)
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
  def getRequestAgentById(id, state = "PENDING"):
    try:
      return RequestAgentTable.objects.get(request_id = id, state = state)
    except Exception as e:
      return None