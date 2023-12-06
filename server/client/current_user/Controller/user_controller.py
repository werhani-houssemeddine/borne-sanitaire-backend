from lib.HTTP import HTTP_REQUEST

from lib.token import Token

class UserInfo:
  def __init__(self, username, email, role) -> None:
    self.username = username
    self.email    = email
    self.role     = role

  def isAdmin(self) -> bool:
    return self.role == "ADMIN"
  
  def isAgent(self) -> bool:
    return self.role == "AGENT"


class User:
  def __init__(self, id, username, email, role) -> None:
    self.id   = id
    self.user = UserInfo(username, email, role)

class UserController:
  def __init__(self, request: HTTP_REQUEST) -> None:
    try:
      self.request: HTTP_REQUEST = request
      self.current_user: User    = self.getCurrentUser()
    except Exception as e:
      raise
    
  def getCurrentUser(self) -> User:
    try:
      token = self.request.headers.Authorization
      payload_token = Token.getTokenPayload(token)
      return User(
        id       = payload_token['id'],
        username = payload_token['username'],
        email    = payload_token['email'],
        role     = payload_token['role']
      )
    except Exception as e:
      raise
  
  def toJSON(self):
    user = self.current_user.user
    return {
      'id': self.current_user.id,
      'user': {
        'username'   : user.username,
        'email'      : user.email,
        'role'       : user.role,
        'is_admin'   : user.role == "ADMIN",
        'is_agent'   : user.role == "AGENT",
        'permessions': []
      }
    }
    