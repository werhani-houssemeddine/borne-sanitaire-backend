from lib.errors import ServerError, ValidationError
from lib.HTTP   import HTTP_REQUEST, HTTP_RESPONSE, RESPONSE_SAMPLE

from client.admin.Controller import AddNewRequestAgentController
from client.admin.Service    import SendEmailToAgent 
class RequestAgentAdminMiddleware:
  @staticmethod
  def sendNewRequest(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    try:
      request_agent = AddNewRequestAgentController(request)
      request_id    = request_agent.getRequestId()
      print('TI TA7KI BERRASMI')
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