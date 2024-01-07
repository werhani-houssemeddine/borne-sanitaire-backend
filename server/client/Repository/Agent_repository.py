from lib.errors import ValidationError

from client.models import AgentModel, UserModel

class SelectAgent:
  @staticmethod
  def _get_agent_by_attribute(attribute, value):
    try:
      return AgentModel.objects.get(**{attribute: value})
    except AgentModel.DoesNotExist:
      raise ValidationError(field = attribute, message = f"{attribute} DOES NOT EXIST")
    except Exception:
      raise

  @staticmethod
  def getAgentById(id) -> AgentModel:
    try:
      return SelectAgent._get_agent_by_attribute('id', id)
    
    except ValidationError: raise
    except Exception: raise

  @staticmethod
  def getAgentByAgentId(agent_id) -> AgentModel:
    try:
      return SelectAgent._get_agent_by_attribute('agent_id', agent_id)
    
    except AgentModel.DoesNotExist: raise ValidationError('AGENT', 'AGENT DOES NOT EXIST')
    except ValidationError: raise
    except Exception: raise

  @staticmethod
  def getAllAgents(user_id) -> list[AgentModel] | None:
    try:
      return AgentModel.objects.filter(user_id=user_id)
      
    except AgentModel.DoesNotExist: return None
    except Exception: raise

  @staticmethod
  def getSuspendAgents(user_id) -> list[AgentModel] | None:
    try:
      return AgentModel.objects.filter(
        user_id = user_id,
        suspend = True
      )
    except AgentModel.DoesNotExist: return None
    except Exception: raise

  @staticmethod
  def getAcitiveAgents(user_id) -> list[AgentModel] | None:
    try:
      return AgentModel.objects.filter(
        user_id = user_id,
        suspend = False
      )
    
    except AgentModel.DoesNotExist: return None
    except Exception: raise 



class UpdateAgent:
  @staticmethod
  def _update_user_attribute(id, attribute, new_value, model_class):
    try:
      user = model_class.objects.get(id=id)
      setattr(user, attribute, new_value)
      user.save()
    except model_class.DoesNotExist:
      raise ValidationError('AGENT', 'INVALID AGENT ID')
    except Exception as e:
      raise ValidationError(attribute, 'INVALID ATTRIBUTE PROPERTY')

  @staticmethod
  def updateUserPassword(id, new_password):
    UpdateAgent._update_user_attribute(id, 'password', new_password, UserModel)

  @staticmethod
  def updateUserUsername(id, new_username):
    UpdateAgent._update_user_attribute(id, 'user_name', new_username, UserModel)

  @staticmethod
  def suspendAgent(agent_id):
    UpdateAgent._update_user_attribute(agent_id, 'suspend', True, AgentModel)

  @staticmethod
  def unsuspendAgent(agent_id):
    UpdateAgent._update_user_attribute(agent_id, 'suspend', False, AgentModel)

  @staticmethod
  def deleteAgents(user_id):
    return AgentModel.objects.filter(user_id = user_id).delete()

class AddNew:
  @staticmethod
  def makeNewAgent(user_id: UserModel, agent_id: UserModel) -> AgentModel:
    try:
      return AgentModel.objects.create(user_id  = user_id, agent_id = agent_id)
      
    except Exception as e:
      print(e)
      return None



class AgentRepository:
  getAgentById      = SelectAgent.getAgentById
  getAgentByAgentId = SelectAgent.getAgentByAgentId
  getAllAgents      = SelectAgent.getAllAgents
  getActiveAgents   = SelectAgent.getAcitiveAgents
  getSuspendAgents  = SelectAgent.getSuspendAgents

  updateUserPassword = UpdateAgent.updateUserPassword
  updateUserUsername = UpdateAgent.updateUserUsername
  unsuspendAgent     = UpdateAgent.unsuspendAgent
  suspendAgent       = UpdateAgent.suspendAgent

  addNewAgent        = AddNew.makeNewAgent

  deleteAgentsByUserId = UpdateAgent.deleteAgents