from lib.HTTP   import HTTP_REQUEST, RESPONSE_SAMPLE
from lib.errors import ValidationError

from client.authentication.Controller import OTPController

class OTPMiddleware:
  @staticmethod
  def enableOTP(request: HTTP_REQUEST) -> RESPONSE_SAMPLE:
    try:
      OTPController.enable_disable_OTP(request = request, is_enabled = True)
      return RESPONSE_SAMPLE.OK({ 'enbled_otp': True })

    except ValidationError as ve:
      return RESPONSE_SAMPLE.BAD_REQUEST({ str(ve.field): str(ve.message) })
    except Exception as e:
      return RESPONSE_SAMPLE.BAD_REQUEST()

  @staticmethod
  def disableOTP(request: HTTP_REQUEST) -> RESPONSE_SAMPLE:
    try:
      OTPController.enable_disable_OTP(request = request, is_enabled = False)
      return RESPONSE_SAMPLE.OK({ 'enbled_otp': True })
      
    except ValidationError as ve:
      return RESPONSE_SAMPLE.BAD_REQUEST({ str(ve.field): str(ve.message) })
    except Exception as e:
      return RESPONSE_SAMPLE.BAD_REQUEST()

  
  @staticmethod
  def checkOTP(request: HTTP_REQUEST) -> RESPONSE_SAMPLE:
    try:
      OTPController.checkOTP(request = request)

    except Exception as e:
      return RESPONSE_SAMPLE.BAD_REQUEST()
