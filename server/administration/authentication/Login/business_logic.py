class InvalidInputException(Exception):
  pass

class LoginBusinessLayer:

  # This method will check user credentials, it will raise 
  # an exception if the user send invalid credentials
  # otherwise it will return the user's email and password
  @staticmethod 
  def validate_login_data(email = None, password = None):
    try:
      if email == None:
        raise InvalidInputException('Email is required')
      
      if password == None:
        raise InvalidInputException('Password is required')
      
      if not isinstance(email, str) or '@' not in email:
        raise InvalidInputException('email must be a valid email address \'str\' type and contains @ characters')
      
      if not isinstance(password, str) or len(password) < 10:
        raise InvalidInputException('Password must be at least 10 characters')
      
      return (email.lower(), password)

    except Exception as e:
      print(e)
      raise
    
  # this method will not checking email or password it is the developer's responsibility
  # to ensure that email and password are valid, the function will just ensure that 
  # email and password are correct 
  @staticmethod
  def check_credentials(email, password):
    return email == 'houssemwuerhani@gmail.com' and password == '_00aa123452002_'