class User:
  def __init__(self, email, password) -> None:
    self.email    = email
    self.password = password

class HandleError:
  def __init__(self, error: bool, message):
    self.error   = error
    self.message = message

class LoginController:
  
  @staticmethod
  def checkPayload(data):

    if 'email' not in data:
      return HandleError(True, 'Please enter an email address')

    if 'password' not in data:
      return HandleError(True, 'Please enter a password')
    
    return User(data['email'], data['password'])

  @staticmethod
  def checkCredentials(email, password):
    if '@' not in email:
      return HandleError(True, 'Please enter a valid email address')
    
    if len(password) < 8:
      return HandleError(True, 'Password must be at least 8 characters')
    
    return HandleError(error = False, message = 'Credentials are valid')


  @staticmethod
  def verifyCredentials(email, password):
    isCredentialsValid = LoginController.checkCredentials(email, password)

    if(isCredentialsValid.error == True):
      return isCredentialsValid
    
    if email == "houssem@gmail.com" and password == "123456789":
      return HandleError(error = False, message = 'Credentials are correct')
    else:
      return HandleError(error = True, message = 'Email or password are incorrect')