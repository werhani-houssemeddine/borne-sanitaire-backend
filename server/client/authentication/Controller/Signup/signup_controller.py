from lib.HTTP   import HTTP_REQUEST
from lib.bcrypt import Bcrypt
from lib.token  import Token

from .signup_validate import SignupControllerValidatorAdmin
from .signup_validate import SignupControllerValidatorAgent

from client.Repository import UserRepository, DeviceRepository, OTP_Repository
from client.Repository import RequestAgentRepository, NotificationPreferencesRepository

from client.models     import UserModel, AgentModel


from lib.errors   import ValidationError, Validator

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
  
  @staticmethod
  def initializeNotificationPreferenceTable(user: UserModel):
    try:
      if user.role == "AGENT": 
        NotificationPreferencesRepository.initAgentNotification(agent = user)
      elif user.role == "ADMIN": 
        NotificationPreferencesRepository.initAdminNotification(admin = user)
    
      raise ValidationError("role", "Invalid user role")

    except Exception: raise

class SignupControllerAgent(SignupController):
  def __init__(self, request: HTTP_REQUEST) -> None:
    try:
      super().__init__(request)
      agent = SignupControllerValidatorAgent(request)
      self.agent = self.createNewAgent(agent)

      #? Initialize notification table
      self.initializeNotificationPreferenceTable(self.agent.agent_id)

    except Exception: raise
  
    
  def createNewAgent(self, agent: SignupControllerValidatorAgent) -> AgentModel:
    try:
      #? Update the request agent state
      RequestAgentRepository.updateRequestAgentState(agent.request_agent_id, "ACCEPT")
      
      #? Get the user
      user = agent.request_agent.user_id

      #? Create the new agent
      return self._createNewAgent(agent = agent, user = user)
    
    except Exception:
      raise
      

class SignupControllerAdmin(SignupController):
  def __init__(self, request: HTTP_REQUEST) -> None:
    super().__init__(request)
    try:
      admin      = SignupControllerValidatorAdmin(request)
      admin_data = self.createNewAdmin(admin)
      self.initializeDeviceToAdmin(admin_data, admin)
      self.initializeNotificationPreferenceTable(admin_data)
      self.admin = admin_data
    except Exception as e:
      raise
    
  def createNewAdmin(self, admin: SignupControllerValidatorAdmin) -> UserModel:
    return self._createNewAdmin(admin)
  
  @staticmethod
  def initializeDeviceToAdmin(user: UserModel, admin: SignupControllerValidatorAdmin):
    DeviceRepository.addDevice(admin.device_id, user, main_device = True)

  @staticmethod
  def SignupEmailAdmin(request: HTTP_REQUEST):
    try:
      email = request.body.get('email')
      Validator({ 'email': email }).check_not_null('email').check_not_empty('email').check_email('email')

      if UserRepository.getUserByEmail(email) == None:
        return {
          'email': email,
          'code' : OTP_Repository.createNewOTP(email)
        }
            
      else:
        raise ValidationError('email', 'This email already used')

    except Exception:
      raise
  