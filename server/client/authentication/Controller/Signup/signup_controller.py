from lib.HTTP   import HTTP_REQUEST
from lib.bcrypt import Bcrypt

from .signup_validate import SignupControllerValidatorAdmin
from .signup_validate import SignupControllerValidatorAgent

from client.Repository import UserRepository, DeviceRepository, RequestAgentRepository
from client.models     import UserModel

class SignupController:
  def __init__(self, request: HTTP_REQUEST) -> None:
    self.request = request

  def createNewUser(
      self, 
      baseController: SignupControllerValidatorAdmin | SignupControllerValidatorAgent, 
      role: str
    ) -> UserModel:
      return UserRepository.createNewUser(
        user_name = baseController.user_name,
        password  = self.hash_password(baseController.password),
        email     = baseController.email,
        role      = role
      )

  def hash_password(self, password: str) -> str:
    hashed_password = Bcrypt.hash(password)
    return hashed_password.decode('utf-8')


class SignupControllerAgent(SignupController):
  def __init__(self, request: HTTP_REQUEST) -> None:
    super().__init__(request)
    agent = SignupControllerValidatorAgent(request)
    self.createNewAgent(agent)
    
  def createNewAgent(self, agent: SignupControllerValidatorAgent) -> UserModel:
    self.updateAgentRequestState(agent.request_agent_id)
    return self.createNewUser(agent, role = agent.role)
      
  def updateAgentRequestState(agent_id) -> bool:
    return RequestAgentRepository.updateRequestAgentState(agent_id, "ACCEPT") 

class SignupControllerAdmin(SignupController):
  def __init__(self, request: HTTP_REQUEST) -> None:
    super().__init__(request)
    try:
      admin      = SignupControllerValidatorAdmin(request)
      admin_data = self.createNewAdmin(admin)
      self.initializeDeviceToAdmin(admin_data, admin)
    except Exception as e:
      raise
    
  def createNewAdmin(self, admin: SignupControllerValidatorAdmin) -> UserModel:
    return self.createNewUser(admin, role = admin.role)
  
  @staticmethod
  def initializeDeviceToAdmin(user: UserModel, admin: SignupControllerValidatorAdmin):
    DeviceRepository.addDevice(admin.device_id, user)
