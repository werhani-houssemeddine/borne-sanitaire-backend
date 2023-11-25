from lib.HTTP import HTTP_REQUEST, HTTP_RESPONSE

class AgentAdminMiddleware:
  @staticmethod
  def getOneAgent(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    pass

  @staticmethod
  def getAllAgent(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    pass

  @staticmethod
  def setAgentPermissions(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    pass

  @staticmethod
  def suspendCurrentAgent(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    pass

  @staticmethod
  def unsuspendCurrentAgent(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    pass
  