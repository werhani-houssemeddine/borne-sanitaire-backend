from lib.errors    import ValidationError
from client.models import UserModel


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
  def createNewUser(email: str, password: str, user_name: str, role: str):
    return UserModel.objects.create(
      user_name = user_name,
      email     = email,
      password  = password,
      role      = role
    )

  @staticmethod
  def createNewAgent(email: str, password: str, user_name: str):
    return UserRepository.createNewUser(email, password, user_name, "AGENT")
  
  @staticmethod
  def createNewAdmin(email: str, password: str, user_name: str):
    return UserRepository.createNewUser(email, password, user_name, "ADMIN")