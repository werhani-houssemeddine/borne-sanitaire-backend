from lib.HTTP   import HTTP_REQUEST
from lib.bcrypt import Bcrypt
from lib.token  import Token

from .signup_validate import SignupControllerValidatorAdmin
from .signup_validate import SignupControllerValidatorAgent

from client.Repository import UserRepository, DeviceRepository
from client.Repository import RequestAgentRepository, AgentRepository

from client.models     import UserModel, AgentModel

class SignupController:
  def __init__(self, request: HTTP_REQUEST) -> None:
    self.request = request

  #? Create new Admin
  def _createNewAdmin(self, admin: SignupControllerValidatorAdmin) -> UserModel:
    return UserRepository.createNewAdmin(
      user_name = admin.user_name,
      password  = self.hash_password(admin.password),
      email     = admin.email
    )
  
  #? Create new Agent
  def _createNewAgent(self, agent: SignupControllerValidatorAgent, user: UserModel) -> AgentModel:
    return UserRepository.createNewAgent(
      user_name = agent.user_name,
      password  = self.hash_password(agent.password),
      email     = agent.email,
      user      = user
    )

  def hash_password(self, password: str) -> str:
    hashed_password = Bcrypt.hash(password)
    return hashed_password.decode('utf-8')
  
  @staticmethod
  def generateToken(user: UserModel) -> bytes:
    payload = { 'email': user.email, 'id': user.id, 'username': user.user_name, 'role': user.role }
    return Token.createToken(payload)


class SignupControllerAgent(SignupController):
  def __init__(self, request: HTTP_REQUEST) -> None:
    try:
      super().__init__(request)
      agent = SignupControllerValidatorAgent(request)
      self.agent = self.createNewAgent(agent)
      
    except Exception: raise
    
  def createNewAgent(self, agent: SignupControllerValidatorAgent) -> AgentModel:
    try:
      #? Update the request agent state
      # self.updateAgentRequestState(agent.request_agent_id)
      
      #? Get the user
      user = agent.request_agent.user_id

      #? Create the new agent
      return self._createNewAgent(agent = agent, user = user)
    
    except Exception:
      raise
      
  @staticmethod
  def updateAgentRequestState(agent_id) -> bool:
    return RequestAgentRepository.updateRequestAgentState(agent_id, "ACCEPT")

class SignupControllerAdmin(SignupController):
  def __init__(self, request: HTTP_REQUEST) -> None:
    super().__init__(request)
    try:
      admin      = SignupControllerValidatorAdmin(request)
      admin_data = self.createNewAdmin(admin)
      self.initializeDeviceToAdmin(admin_data, admin)
      self.admin = admin_data
    except Exception as e:
      raise
    
  def createNewAdmin(self, admin: SignupControllerValidatorAdmin) -> UserModel:
    return self._createNewAdmin(admin)
  
  @staticmethod
  def initializeDeviceToAdmin(user: UserModel, admin: SignupControllerValidatorAdmin):
    DeviceRepository.addDevice(admin.device_id, user)
