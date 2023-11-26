from lib.errors import ServerError, ValidationError
from lib.HTTP   import HTTP_REQUEST, HTTP_RESPONSE, RESPONSE_SAMPLE

from client.agent.Controller import RequestAgentController

class RequestAgentMiddleware:
  @staticmethod
  def rejectRequest(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    try:
      result: bool = RequestAgentController.reject(request)
      return RESPONSE_SAMPLE.OK(data = { 'delete': result })
        
    except ValidationError as ve:
      return RESPONSE_SAMPLE.BAD_REQUEST({ str(ve.field): str(ve.message) })
    
    except Exception as e:
      print(e)
      return RESPONSE_SAMPLE.BAD_REQUEST()