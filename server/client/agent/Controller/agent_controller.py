from lib.errors import ServerError, ValidationError
from lib.HTTP   import HTTP_REQUEST

from client.Repository import AgentRepository
from client.models     import AgentModel 

def getUserId(request: HTTP_REQUEST) -> int:
  currentUser = request.session.get('__currentUser__')  
  if currentUser and 'id' in currentUser:
    return int(currentUser['id'])
      
  raise ServerError('USER', 'USER OR USER_ID IS MISSING IN AN AUTHORIZED ENDPOINT')

class AgentController:
  def __init__(self, request: HTTP_REQUEST) -> None:
    self.request = request
    self.user_id = getUserId(request)

  def getAllAgents(self): 
    try:
      listOfAgents = AgentRepository.getAllAgents(self.user_id)
      return list(
        map(AgentController.formatAgentResponse, listOfAgents)
      )
    
    except Exception as e:
      print(f"AN ERROR OCCUREND AgentController.getAllAgents {e}")

  def getSingleAgent(self):
    try:
      agent_id = self.request.params.get('agent_id')
      if agent_id is None: raise ValidationError('ID', 'INVALID AGENT ID')
      
      agent = AgentRepository.getAgentByAgentId(agent_id)
      if agent.user_id != self.user_id:
        raise ValidationError('UNATHORIZED', 'AGENT ID')
      
      return AgentController.formatAgentResponse(agent)

    except ValidationError: raise
    except ServerError: raise
    except Exception: raise
  
  def getActiveAgents(self):
    try:
      listOfActiveAgents = AgentRepository.getActiveAgents(self.user_id)
      return list(
        map(AgentController.formatAgentResponse, listOfActiveAgents)
      )
    
    except Exception as e:
      print(f"AN ERROR OCCUREND AgentController.getActiveAgents {e}")

  def getSuspendAgents(self):
    try:
      listOfSuspendAgents = AgentRepository.getSuspendAgents(self.user_id)
      return list(
        map(AgentController.formatAgentResponse, listOfSuspendAgents)
      )
    
    except Exception as e:
      print(f"AN ERROR OCCUREND AgentController.getActiveAgents {e}")

  

  @staticmethod
  def formatAgentResponse(agent: AgentModel) -> dict:
    
    return {
      'admin_id'   : agent.user_id.id,
      'agent_id'   : agent.agent_id.id,
      'agent_email': agent.agent_id.email,
      'user_name'  : agent.agent_id.user_name,
      'active'     : agent.suspend == False 
    }