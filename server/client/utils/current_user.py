class User:
  def __init__(self, email, username, id, role) -> None:
    self.email = email
    self.username = username
    self.id = id
    self.role = role
  
  getUsername = lambda self: self.username
  getEmail    = lambda self: self.email
  getRole     = lambda self: self.role
  getId       = lambda self: self.id


class CurrentUser(User):
  def __init__(self, email, username, id, role, phoneNumber = None, permessions = None) -> None:
    super().__init__(email, username, id, role)
    self.phoneNumber = phoneNumber
    self.permissions = permessions

  getPermessions = lambda self: self.permissions
  getPhoneNumber = lambda self: self.phoneNumber