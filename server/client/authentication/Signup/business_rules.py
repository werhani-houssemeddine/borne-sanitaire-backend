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

  def username(username: str):
    if len(username) == 0:
      raise ValueError("EMPTY USERNAME")
    return Check

  def role(role: str) -> None:
    if role != "ADMIN" and role != "AGENT":
      raise ValueError("INVALID ROLE TYPE")
    return Check

class SingUp:
  @staticmethod
  def extractUserData(data: dict) -> tuple:
    user_name = data.get('user_name')
    password  = data.get('password')
    email     = data.get('email')
    role      = data.get('role')

    if email is None:
      raise ValueError("Email IS REQUIRED")
    
    if password is None:
      raise ValueError("PASSWORD IS REQUIRED")
    
    if user_name is None:
      raise ValueError("USER_NAME IS REQUIRED")
    
    if role is None:
      raise ValueError("ROLE IS REQUIRED")
    
    return (email, password, user_name, role)
  

  @staticmethod
  def validateUserData(data: dict):
    try:
      (email, password, user_name, role) = SingUp.extractUserData(data)
      
      Check.email(email) \
        .password(password) \
        .username(user_name) \
        .role(role)
      
      return (email, password, user_name, role)

    except Exception as e:
      raise