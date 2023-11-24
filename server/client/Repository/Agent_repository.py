from client.models import Agent as AgentTable
from client.models import User  as UserTable

class SelectAgent:
  @staticmethod
  def _get_agent_by_attribute(attribute, value):
    try:
      return AgentTable.objects.get(**{attribute: value})
    except AgentTable.DoesNotExist:
      return None

  staticmethod
  def getAgentById(id):
    return SelectAgent._get_agent_by_attribute('id', id)
  
  @staticmethod
  def getAgentByAgentId(agent_id):
    return SelectAgent._get_agent_by_attribute('agent_id', agent_id)
    
  @staticmethod
  def getAgentByUserId(user_id):
    return SelectAgent._get_agent_by_attribute('user_id', user_id)


class UpdateAgent:
  @staticmethod
  def _update_user_attribute(id, attribute, new_value, model_class):
    try:
      user = model_class.objects.get(id=id)
      setattr(user, attribute, new_value)
      user.save()
    except model_class.DoesNotExist:
      pass

  @staticmethod
  def updateUserPassword(id, new_password):
      UpdateAgent._update_user_attribute(id, 'password', new_password, UserTable)

  @staticmethod
  def updateUserUsername(id, new_username):
      UpdateAgent._update_user_attribute(id, 'user_name', new_username, UserTable)

  @staticmethod
  def suspendAgent(agent_id):
      UpdateAgent._update_user_attribute(agent_id, 'suspend', True, AgentTable)

  @staticmethod
  def unsuspendAgent(agent_id):
      UpdateAgent._update_user_attribute(agent_id, 'suspend', False, AgentTable)

class AddNew:
  @staticmethod
  def makeNewUser(user_id, user_name, email, password, role):
    try:
      new_user = UserTable.objects.create(
        user_name = user_name,
        password  = password,
        email     = email,
        role      = role
      )

      if role == "ADMIN":
        return new_user
      
      return AgentTable.objects.create(user_id  = user_id, agent_id = new_user.id)
      
    except Exception as e:
      return None



class AgentRepository:
  getAgentById      = SelectAgent.getAgentById
  getAgentByAgentId = SelectAgent.getAgentByAgentId
  getAgentByUserId  = SelectAgent.getAgentByUserId

  updateUserPassword = UpdateAgent.updateUserPassword
  updateUserUsername = UpdateAgent.updateUserUsername
  unsuspendAgent     = UpdateAgent.unsuspendAgent
  suspendAgent       = UpdateAgent.suspendAgent

  addNewUser = AddNew.makeNewUser