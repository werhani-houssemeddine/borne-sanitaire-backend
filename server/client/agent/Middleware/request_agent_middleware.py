from lib.HTTP import HTTP_REQUEST, HTTP_RESPONSE

class RequestAgentMiddleware:
  @staticmethod
  def acceptRequest(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    pass

  @staticmethod
  def rejectRequest(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    pass