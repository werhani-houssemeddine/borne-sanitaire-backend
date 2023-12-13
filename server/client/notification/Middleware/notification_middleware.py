from lib.errors import ValidationError
from lib.HTTP   import HTTP_REQUEST, RESPONSE_SAMPLE, HTTP_RESPONSE

from client.notification.Controller import NotificationPreferencesController

class NotificationPreferencesMiddleware:
  @staticmethod
  def getNotificationPreferences(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    try:
      n = NotificationPreferencesController.getNotificationPreference(request)
      return RESPONSE_SAMPLE.OK(n)
    
    except ValidationError as ve:
      return RESPONSE_SAMPLE.BAD_REQUEST({ str(ve.field): str(ve.message) })
    except Exception:
      return RESPONSE_SAMPLE.BAD_REQUEST()


  @staticmethod
  def updateNotificationPreferences(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    try:
      updated = NotificationPreferencesController.updateNotificationPreference(request)
      
      if updated == None:
        return RESPONSE_SAMPLE.BAD_REQUEST({ 'Property': 'INVALID PROPERTY' })

      return RESPONSE_SAMPLE.OK({ 'updated': updated })
    
    except ValidationError as ve:
      return RESPONSE_SAMPLE.BAD_REQUEST({ str(ve.field): str(ve.message) })
    except Exception as e:
      print(e)
      return RESPONSE_SAMPLE.BAD_REQUEST()
