from lib.HTTP import HTTP_REQUEST, HTTP_RESPONSE

class AgentMiddleware:
  @staticmethod
  def getCurrentAgent(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    pass

  @staticmethod
  def updateCurrentAgentPassword(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    pass

  @staticmethod
  def updateCurrentAgentUsername(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    pass

  @staticmethod
  def suspendCurrentAgent(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    pass
  