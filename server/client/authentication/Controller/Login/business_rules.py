class Check:
  @staticmethod
  def email(email: str):
    if '@' not in email or '.' not in email or len(email) < 6:
      raise ValueError('INAVALID EMAIL')
    return Check

  def password(password: str):
    if len(password) < 8:
      raise ValueError("INVALID PASSWORD LENGTH")
    return Check


class LogIn:
  @staticmethod
  def extractUserData(data: dict) -> tuple:
    password  = data.get('password')
    email     = data.get('email')

    if email is None:
      raise ValueError("Email IS REQUIRED")
    
    if password is None:
      raise ValueError("PASSWORD IS REQUIRED")
    
    return (email, password)
  

  @staticmethod
  def validateUserData(data: dict):
    try:
      (email, password) = LogIn.extractUserData(data)
      Check.email(email).password(password) # This class will check if data is valid
      
      return (email, password)

    except Exception as e:
      raise