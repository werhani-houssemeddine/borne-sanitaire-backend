from lib.errors import ServerError, ValidationError
from lib.HTTP   import HTTP_REQUEST, HTTP_RESPONSE, RESPONSE_SAMPLE

from client.agent.Controller import AgentController
      

class GetAgentMiddleware:
  @staticmethod
  def getAllAgents(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    try:
      agentController = AgentController(request)
      listOfAgents    = agentController.getAllAgents()
      
      if listOfAgents == None:
        return RESPONSE_SAMPLE.OK(data = [])
      
      return RESPONSE_SAMPLE.OK(data = listOfAgents )

    except ServerError as se: 
      return RESPONSE_SAMPLE.SERVER_ERROR()
    except ValidationError as ve:
      return RESPONSE_SAMPLE.BAD_REQUEST(details = { str(ve.field): str(ve.message) })
    except Exception: return RESPONSE_SAMPLE.BAD_REQUEST()

  @staticmethod 
  def getOneAgent(request: HTTP_REQUEST) -> HTTP_REQUEST:
    try:
      agentController = AgentController(request)
      agent           = agentController.getSingleAgent()    
      
      return RESPONSE_SAMPLE.OK(data = agent )

    except ServerError as se: 
      return RESPONSE_SAMPLE.SERVER_ERROR()
    except ValidationError as ve:
      return RESPONSE_SAMPLE.BAD_REQUEST(details = { str(ve.field): str(ve.message) })
    except Exception: return RESPONSE_SAMPLE.BAD_REQUEST()

  @staticmethod
  def getActiveAgents(request: HTTP_REQUEST) -> HTTP_REQUEST:
    try:
      agentController    = AgentController(request)
      listOfActiveAgents = agentController.getActiveAgents()
      
      if listOfActiveAgents == None:
        return RESPONSE_SAMPLE.OK(data = [])
      
      return RESPONSE_SAMPLE.OK(data = listOfActiveAgents )

    except ServerError as se: 
      return RESPONSE_SAMPLE.SERVER_ERROR()
    except ValidationError as ve:
      return RESPONSE_SAMPLE.BAD_REQUEST(details = { str(ve.field): str(ve.message) })
    except Exception: return RESPONSE_SAMPLE.BAD_REQUEST()

  @staticmethod
  def getArchivedAgents(request: HTTP_REQUEST) -> HTTP_REQUEST:
    try:
      agentController     = AgentController(request)
      listOfSuspendAgents = agentController.getSuspendAgents()
      
      if listOfSuspendAgents == None:
        return RESPONSE_SAMPLE.OK(data = [])
      
      return RESPONSE_SAMPLE.OK(data = listOfSuspendAgents )

    except ServerError as se: 
      return RESPONSE_SAMPLE.SERVER_ERROR()
    except ValidationError as ve:
      return RESPONSE_SAMPLE.BAD_REQUEST(details = { str(ve.field): str(ve.message) })
    except Exception: return RESPONSE_SAMPLE.BAD_REQUEST()

  @staticmethod
  def getPendingAgents(request: HTTP_REQUEST) -> HTTP_REQUEST:
    pass