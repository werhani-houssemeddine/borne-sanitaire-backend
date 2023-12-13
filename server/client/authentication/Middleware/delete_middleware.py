from lib.HTTP   import HTTP_REQUEST, RESPONSE_SAMPLE
from lib.errors import ValidationError

from client.authentication.Controller import OTPController, DeleteAccountController

def DeleteAccountMiddleware(request: HTTP_REQUEST) -> RESPONSE_SAMPLE:
  try:
    DeleteAccountController(request = request)
    return RESPONSE_SAMPLE.OK({ 'deleted': True })

  except ValidationError as ve:
    return RESPONSE_SAMPLE.BAD_REQUEST({ str(ve.field): str(ve.message) })
  except Exception as e:
    print(e)
    return RESPONSE_SAMPLE.BAD_REQUEST()