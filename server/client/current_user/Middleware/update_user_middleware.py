from lib.errors import ValidationError
from lib.HTTP   import HTTP_REQUEST, RESPONSE_SAMPLE

from client.current_user.Controller import UpdateUserController

class UpdateUserMiddleware:
  @staticmethod
  def updateUsername(request: HTTP_REQUEST):
    try:
      update = UpdateUserController(request)
      if update.updateUsername():
        return RESPONSE_SAMPLE.OK({ 'username': 'updated successfully' })
    
    except ValidationError as ve:
      return RESPONSE_SAMPLE.BAD_REQUEST({ str(ve.field): str(ve.message) })
    except Exception:
      return RESPONSE_SAMPLE.BAD_REQUEST()

  @staticmethod
  def updatePassword(request: HTTP_REQUEST):
    try:
      update = UpdateUserController(request)
      if update.updatePassword():
        return RESPONSE_SAMPLE.OK({ 'password': 'updated successfully' })

    except ValidationError as ve:
      print(ve)
      return RESPONSE_SAMPLE.BAD_REQUEST({ str(ve.field): str(ve.message) })
    except Exception as e:
      return RESPONSE_SAMPLE.BAD_REQUEST()

  @staticmethod
  def updatePhoneNumber(request: HTTP_REQUEST):
    try:
      update = UpdateUserController(request)
      if update.updatePhoneNumber():
        return RESPONSE_SAMPLE.OK({ 'phone_number': 'updated successfully' })
    
    except ValidationError as ve:
      return RESPONSE_SAMPLE.BAD_REQUEST({ str(ve.field): str(ve.message) })
    except Exception:
      return RESPONSE_SAMPLE.BAD_REQUEST()
    
  @staticmethod
  def updateProfilePhoto(request: HTTP_REQUEST):
    pass
