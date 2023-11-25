from lib.HTTP import HTTP_REQUEST, HTTP_RESPONSE

class RequestAgentAdminMiddleware:
  @staticmethod
  def getOneRequest(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    pass

  @staticmethod
  def getAllRequest(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    pass

  @staticmethod
  def deleteRequest(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    pass

  #! For future version may the admin set the time for request to be in pending state default time is 7days
  # @staticmethod
  # def updateRequest(request: HTTP_REQUEST) -> HTTP_RESPONSE:
  #   pass