from lib.HTTP import HTTP_REQUEST, RESPONSE_SAMPLE

from client.admin.Controller import DeviceController

class DeviceMiddleware:
  @staticmethod
  def checkDeviceDisponibility(request: HTTP_REQUEST):
    try:
      is_device_exist = DeviceController.checkDevice(request)
      if is_device_exist:
        return RESPONSE_SAMPLE.ok({ 'device_exist': True })
      
      return RESPONSE_SAMPLE.badRequest({ 'details': 'EXPIRED OR NOT FOUND DEVICE' })

    except Exception as e:
      return RESPONSE_SAMPLE.badRequest({ 'details': str(e) })