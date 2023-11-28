from lib.HTTP     import HTTP_REQUEST, HTTP_RESPONSE, RESPONSE_SAMPLE
from lib.errors   import ValidationError

from client.authentication.Controller import SignupControllerAdmin

def SignupAdminMiddleware(request: HTTP_REQUEST) -> HTTP_RESPONSE:
  try:    
    user_signup = SignupControllerAdmin(request)
    if user_signup:
      token = SignupControllerAdmin.generateToken(user_signup.admin)
      return RESPONSE_SAMPLE.OK(data = { 'token': token })
    
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
  