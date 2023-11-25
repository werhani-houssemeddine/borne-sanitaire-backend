from lib.HTTP import HTTP_REQUEST, HTTP_RESPONSE

class UserMiddleware:
  @staticmethod
  def getCurrentUser(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    pass

  @staticmethod
  def updateCurrentUserUsername(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    pass

  @staticmethod
  def updateCurrentUserPassword(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    pass

  @staticmethod
  def updateCurrentUserPhoneNumber(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    pass
  