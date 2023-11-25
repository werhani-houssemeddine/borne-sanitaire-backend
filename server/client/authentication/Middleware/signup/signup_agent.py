from lib.HTTP     import HTTP_REQUEST, HTTP_RESPONSE, RESPONSE_SAMPLE
from lib.errors   import ValidationError

from client.authentication.Controller import SignupControllerAgent

def SignupAgentMiddleware(request: HTTP_REQUEST) -> HTTP_RESPONSE:
  try:    
    if SignupControllerAgent(request):
      return RESPONSE_SAMPLE.OK()
    
    else:
      return RESPONSE_SAMPLE.faillureBuild(
        status_code = 401,
        message     = "UNAUTHORIZED",
        data        = { 'User': 'WRONG CREDENTIALS' }
      )

  except ValidationError as ve:
    print(f"AN ERROR OCCURED {ve}")
    return RESPONSE_SAMPLE.BAD_REQUEST({ str(ve.field): str(ve.message) })
  except Exception as e:
    print(f'LoginMiddleware {e}')
    return RESPONSE_SAMPLE.BAD_REQUEST()
  