from lib.errors import ServerError, ValidationError
from lib.HTTP   import HTTP_REQUEST

from client.Repository import AgentRepository, UserPictureRepository
from client.models     import AgentModel, UserPictureModel

from client.utils import getUserId

class SuspendAgent:
  @staticmethod
  def getSuspendedAgents(user_id):
    try:
      listOfSuspendAgents = AgentRepository.getSuspendAgents(user_id)
      return list(
        map(AgentController.formatAgentResponse, listOfSuspendAgents)
      )
    
    except Exception as e: raise
  
  @staticmethod
  def suspendAgent(agent_id):
    try:
      AgentRepository.suspendAgent(agent_id)
      return True
  
    except Exception: raise

  @staticmethod
  def restoreAgent(agent_id):
    try:
      AgentRepository.unsuspendAgent(agent_id)
      return True
    
    except Exception: raise

class AgentController:
  def __init__(self, request: HTTP_REQUEST) -> None:
    self.request  = request
    self.user_id  = getUserId(request)
  
  def getAgent(self) -> AgentModel:
    try:
      id = self.request.params.get('id')
      if id is None: raise ValidationError('ID', 'INVALID AGENT ID')
  
      agent = AgentRepository.getAgentById(id)
      if agent.user_id.id != self.user_id: raise ValidationError('UNATHORIZED', 'AGENT ID')
      
      return agent
    
    except ValidationError: raise
    except ServerError: raise
    except Exception: raise


  def getAllAgents(self): 
    try:
      listOfAgents = AgentRepository.getAllAgents(self.user_id)
      return list(
        map(AgentController.formatAgentResponse, listOfAgents)
      )  
    except Exception as e: raise

  def getSingleAgent(self):
    return AgentController.formatAgentResponse(self.getAgent())

  
  def getActiveAgents(self):
    try:
      listOfActiveAgents = AgentRepository.getActiveAgents(self.user_id)
      return list(
        map(AgentController.formatAgentResponse, listOfActiveAgents)
      )
    
    except Exception as e: raise

  def getSuspendAgents(self):
    return SuspendAgent.getSuspendedAgents(self.user_id)

  def suspendAgent(self):
    try:
      agent = self.getAgent()
      id    = agent.id
      return SuspendAgent.suspendAgent(id)
    
    except ValidationError as ve:
      print({ str(ve.field): str(ve.message) })
      raise
    
    except Exception as e:
      print(e)
      raise

  def restoreAgent(self):
    try:
      agent = self.getAgent()
      id    = agent.id
      return SuspendAgent.restoreAgent(id)
    
    except Exception: raise
  
  def deleteAgent(self):
    try:
      agent = self.getAgent()
      agent.delete()
    
    except Exception as e:
      raise

  @staticmethod
  def getProfilePicture(agent: AgentModel) -> UserPictureModel | None:
    try:
      agent_id = agent.agent_id.id
      picture  = UserPictureRepository.getUserPicture(agent_id)
      
      return None if picture == None else picture.avatar.url
    
    except Exception: return None

  @staticmethod
  def formatAgentResponse(agent: AgentModel) -> dict:
    
    return {
      'admin_id'   : agent.user_id.id,
      'agent_id'   : agent.id,
      'agent_email': agent.agent_id.email,
      'user_name'  : agent.agent_id.user_name,
      'active'     : agent.suspend == False,
      
      'profile_picture': AgentController.getProfilePicture(agent),
      'phone_number'   : agent.agent_id.phone_number,
      'permessions'    : [],
      'created_at'     : agent.created_at
    }
