from client.models import User as UserTable

#! This repository need some try/catch blocks
#! it lacks also of data type validation
class User:
  @staticmethod
  def getUser(*args):
    try:
      return UserTable.objects.get(args)
    except Exception as e:
      print(e)
      return None

  @staticmethod
  def getUserById(id: int):
    return User.getUser({ 'id': id })
  
  @staticmethod
  def getUserByEmail(email: str):
    try:
      return UserTable.objects.get(email = email)
    except Exception as e:
      print(e)
      return None
    
  @staticmethod
  def createNewUser(email: str, password: str, user_name: str, role: str):
    return UserTable.objects.create(
      user_name = user_name,
      email     = email,
      password  = password,
      role      = role
    )

  @staticmethod
  def createNewAgent(email: str, password: str, user_name: str):
    return User.createNewUser(email, password, user_name, "AGENT")
  
  @staticmethod
  def createNewAdmin(email: str, password: str, user_name: str):
    return User.createNewUser(email, password, user_name, "ADMIN")