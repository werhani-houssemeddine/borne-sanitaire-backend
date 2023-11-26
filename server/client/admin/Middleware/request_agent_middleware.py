from lib.errors import ServerError, ValidationError
from lib.HTTP   import HTTP_REQUEST, HTTP_RESPONSE, RESPONSE_SAMPLE

from client.admin.Controller import AddNewRequestAgentController, RequestAgentController
from client.admin.Service    import SendEmailToAgent 

from client.models import RequestAgentModel

class RequestAgentAdminMiddleware:
  @staticmethod
  def sendNewRequest(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    try:
      request_agent = AddNewRequestAgentController(request)
      request_id    = request_agent.getRequestId()
      
      #? Send Email to agent
      SendEmailToAgent.requestAgentEmail(
        username   = request.session['__currentUser__']['username'],
        request_id = request_id,
        email      = request_agent.email,
        ip         = request.ip
      )

      return RESPONSE_SAMPLE.CREATED()

    except ServerError as se:
      return RESPONSE_SAMPLE.SERVER_ERROR()
    except ValidationError as ve:
      return RESPONSE_SAMPLE.BAD_REQUEST({ 'details': str(ve) })
    except Exception as e:
      print(e)
      return RESPONSE_SAMPLE.BAD_REQUEST()
  
  @staticmethod
  def getOneRequest(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    try:
      agent: RequestAgentModel = RequestAgentController.getSingleRequest(request)
      return RESPONSE_SAMPLE.OK(data = agent)
    
    except ServerError as se:
      return RESPONSE_SAMPLE.SERVER_ERROR()
    
    except ValidationError as ve:
      if ve.field == "UNATHORIZED": return RESPONSE_SAMPLE.NOT_AUTHORIZED()
      return RESPONSE_SAMPLE.BAD_REQUEST({ str(ve.field): str(ve.message) })
    
    except Exception as e:
      return RESPONSE_SAMPLE.BAD_REQUEST()


  @staticmethod
  def getAllRequest(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    try:
      listOfRequestAgent = RequestAgentController.getAllRequestAgent(request)
      return RESPONSE_SAMPLE.OK( data = listOfRequestAgent)
    
    except Exception:
      return RESPONSE_SAMPLE.BAD_REQUEST()

  @staticmethod
  def deleteRequest(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    try:
      result: bool = RequestAgentController.deleteRequestAgent(request)
      return RESPONSE_SAMPLE.OK(data = { 'delete': result })
    
    except ServerError as se:
      return RESPONSE_SAMPLE.SERVER_ERROR()
    
    except ValidationError as ve:
      if ve.field == "UNATHORIZED": return RESPONSE_SAMPLE.NOT_AUTHORIZED()
      return RESPONSE_SAMPLE.BAD_REQUEST({ str(ve.field): str(ve.message) })
    
    except Exception as e:
      print(e)
      return RESPONSE_SAMPLE.BAD_REQUEST()

  #! For future version may the admin set the time for request to be in pending state default time is 7days
  # @staticmethod
  # def updateRequest(request: HTTP_REQUEST) -> HTTP_RESPONSE:
  #   pass