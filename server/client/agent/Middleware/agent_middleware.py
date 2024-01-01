from lib.errors import ServerError, ValidationError
from lib.HTTP   import HTTP_REQUEST, HTTP_RESPONSE, RESPONSE_SAMPLE

from .get_agent_middleware import GetAgentMiddleware

from client.agent.Controller import AgentController

class AgentMiddleware(GetAgentMiddleware):
  @staticmethod
  def getCurrentAgent(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    pass

  @staticmethod
  def updateCurrentAgent(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    pass

  @staticmethod
  def updateCurrentAgentPassword(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    pass

  @staticmethod
  def updateCurrentAgentUsername(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    pass

  @staticmethod
  def suspendAgent(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    try:
      agentController = AgentController(request)
      agentController.suspendAgent()

      return RESPONSE_SAMPLE.OK({ 'suspend': True })
    
    except ServerError as se: 
      return RESPONSE_SAMPLE.SERVER_ERROR()
    except ValidationError as ve:
      return RESPONSE_SAMPLE.BAD_REQUEST(details = { str(ve.field): str(ve.message) })
    except Exception: return RESPONSE_SAMPLE.BAD_REQUEST()
  
  @staticmethod
  def restoreAgent(request: HTTP_REQUEST)-> HTTP_RESPONSE:
    try:
      agentController = AgentController(request)
      agentController.restoreAgent()

      return RESPONSE_SAMPLE.OK({ 'restore': True })
    
    except ServerError as se: 
      return RESPONSE_SAMPLE.SERVER_ERROR()
    except ValidationError as ve:
      return RESPONSE_SAMPLE.BAD_REQUEST(details = { str(ve.field): str(ve.message) })
    except Exception: return RESPONSE_SAMPLE.BAD_REQUEST()
  