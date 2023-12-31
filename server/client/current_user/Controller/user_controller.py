from lib.HTTP import HTTP_REQUEST

from lib.token import Token

from client.Repository import UserRepository, UserPictureRepository
from client.models     import UserModel

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
      self.userObject: UserModel = UserRepository.getUserById(self.current_user.id) 
    except Exception as e:
      raise
    
  def getCurrentUser(self) -> User:
    try:
      token = self.request.headers.Authorization
      payload_token = Token.getTokenPayload(token)
      user = UserRepository.getUserById(payload_token['id'])
      return User(
        id       = user.id,
        username = user.user_name,
        email    = user.email,
        role     = user.role
      )
    except Exception as e:
      raise

  def getUserProfilePicture(self) -> str:
    try:
      picture = UserPictureRepository.getUserPicture(self.current_user.id)
      return None if picture == None else picture.avatar.url
    
    except Exception as e:
      return None
  
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
        
        # Permissions will be sent only if the role is agent 
        **({'permissions': []} if user.role == "AGETN" else {}),

        'phone_number': self.userObject.phone_number,
        'created_at'  : self.userObject.created_at,

        'profile_picture': self.getUserProfilePicture()
      }
    }
    