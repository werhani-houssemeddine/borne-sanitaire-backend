from lib.errors import Validator, ValidationError
from lib.HTTP   import HTTP_REQUEST

from client.Repository import RequestAgentRepository, UserRepository, DeviceRepository
from client.models     import RequestAgentModel

class SignupControllerValidatorAdmin:
  def __init__(self, request: HTTP_REQUEST) -> None:
    try:
      (self.email, self.password, self.user_name) = self.extractData(request)
      self.device_id = self.getDeviceId(request)
      self.role      = "ADMIN"

      self.validateUniqueEmail(self.email)

    except ValidationError as ve:
      raise
  
  @staticmethod
  def extractData(request: HTTP_REQUEST) -> tuple[str, str, str]:
    email: str    = request.body.get('email')
    password: str = request.body.get('password')
    username: str = request.body.get('user_name')

    v = lambda field: Validator({'email': email, 'password': password, 'username': username })\
      .check_not_null(field).check_not_empty(field)
    
    v('email').check_email('email')
    v('password').check_min_length('password', 10)
    v('username').check_min_length('username', 4).check_max_length('username', 30)

    return (email, password, username)
  
  @staticmethod
  def getDeviceId(request: HTTP_REQUEST):
    device_id = request.query.get('device')

    if device_id is None:
      raise ValidationError('agent_id', 'MISSING PROPERTY')
    else:
      return SignupControllerValidatorAdmin.validateDeviceId(device_id)
  
  @staticmethod
  def validateUniqueEmail(email) -> str:
    try:
      if UserRepository.getUserByEmail(email):
        raise ValidationError('email', 'EMAIL ALREADY EXIST')
      else:
        return email
    
    except Exception as e:
      raise

  @staticmethod
  def validateDeviceId(device_id) -> str:
    try:
      DeviceRepository.getDeviceById(device_id)
      return device_id
    
    except ValidationError as ve:
      raise ValidationError('DEVICE', 'EXPIRED DEVICE')    
    except Exception as e:
      raise
  
class SignupControllerValidatorAgent:
  def __init__(self, request: HTTP_REQUEST) -> None:
    try:
      (self.user_name, self.password) = self.extractData(request)
      self.request_agent_id = self.getRequestAgentId(request)
      self.role             = "AGENT"
      self.email            = self.getEmail()
    except Exception as e:
      print("HAHAHHAHA EXCEPTION ")

  def extractData(request: HTTP_REQUEST) -> tuple[str, str]:
    password: str = request.body.get('password')
    username: str = request.body.get('user_name')
    
    v = lambda field: Validator({'password': password, 'username': username })\
        .check_not_null(field).check_not_empty(field)
      
    v('password').check_min_length('password', 10)
    v('usermane').check_min_length('username', 4).check_max_length('username', 20)

    return (password, username)
  
  @staticmethod
  def getRequestAgentId(request: HTTP_REQUEST):
    request_agent_id = request.query.get('agent')

    if request_agent_id == None:
      raise ValidationError('agent_id', 'MISSING PROPERTY')
    else:
      return request_agent_id
  
  def getEmail(self) -> str:
    getPendingRequestAgentById = RequestAgentRepository.getPendingRequestAgentById
    agentRequest: RequestAgentModel | None = getPendingRequestAgentById(self.request_agent_id)

    if agentRequest == None:
      raise ValidationError('agent_id', 'EXPIRED REQUEST')
    else:
      return agentRequest.email
   