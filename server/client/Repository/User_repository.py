from lib.errors    import ValidationError
from client.models import UserModel, AgentModel

from .Agent_repository import AgentRepository


#! This repository need some try/catch blocks
#! it lacks also of data type validation
class UserRepository:

  #? Returning the user based on the id 
  #? It will throw an error if not exist
  @staticmethod
  def getUserById(id: int) -> UserModel:
    try:
      return UserModel.objects.get(id = id)
    except UserModel.DoesNotExist:
      raise ValidationError('id', 'This value does not exist')
    except Exception as e:
      print(f'class UserRepository.getUserById error {e}')
      raise ValidationError('id', 'Error retrieving user')
  

  @staticmethod
  def getUserByEmail(email: str):
    try:
      return UserModel.objects.get(email = email)
    except UserModel.DoesNotExist:
      return None
    except Exception as e:
      print(f'class UserRepository.getUserByEmail error {e}')
      raise ValidationError('email', 'Error retrieving user')
    
  @staticmethod
  def getUserByPhoneNumber(phone: int):
    try:
      return UserModel.objects.get(phone_number = phone)
    except UserModel.DoesNotExist:
      return None
    except Exception as e:
      print(f'class UserRepository.getUserByPhoneNumber error {e}')
      raise ValidationError('phone number', 'Error retrieving user')
  

  @staticmethod
  def createNewUser(email: str, password: str, user_name: str, role: str) -> UserModel:
    return UserModel.objects.create(
      user_name = user_name,
      email     = email,
      password  = password,
      role      = role
    )

  #? user is the admin
  @staticmethod
  def createNewAgent(email: str, password: str, user_name: str, user: UserModel) -> AgentModel:
    agent: UserModel = UserRepository.createNewUser(email, password, user_name, "AGENT")
    return AgentRepository.addNewAgent(user_id = user, agent_id = agent)

  
  @staticmethod
  def createNewAdmin(email: str, password: str, user_name: str):
    return UserRepository.createNewUser(email, password, user_name, "ADMIN")
  
  @staticmethod
  def updateUser(id, field: str, value) -> True:
    try:
      user = UserRepository.getUserById(id)
      if field == 'password':
        user.password = value
      elif field == 'user_name':
        user.user_name = value
      elif field == 'phone_number':
        user.phone_number = value

      else:
        raise ValidationError(field, 'INVALID PROPERTY TO UPDATE')
      
      if user.save() == None:
        print(f'Updated {field} ok')
        return True
    
    except ValidationError: raise
    except Exception: raise

  @staticmethod
  def deleteUserById(user_id):
    try:
      return UserRepository.getUserById(user_id).delete()[0]
      

    except ValidationError: raise
    except Exception: raise