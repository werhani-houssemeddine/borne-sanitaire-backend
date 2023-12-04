from lib.errors import ValidationError
from lib.HTTP   import HTTP_REQUEST, RESPONSE_SAMPLE, HTTP_RESPONSE

from client.device.Controller import DeviceController

class DeviceMiddleware:
  @staticmethod
  def isDeviceAvailable(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    try:
      if DeviceController.isDeviceAvailable(request):
        return RESPONSE_SAMPLE.OK({ 'device_exist': True })
      
    except ValidationError as ve:
      print(ve)
      return RESPONSE_SAMPLE.BAD_REQUEST({ str(ve.field): str(ve.message) })
    except Exception as e:
      print(e)
      return RESPONSE_SAMPLE.BAD_REQUEST()