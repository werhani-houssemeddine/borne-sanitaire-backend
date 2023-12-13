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
    
  @staticmethod
  def getDeviceVisitorsNumber(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    max_visitors = DeviceController.getVistorNumber(request)
    return RESPONSE_SAMPLE.OK({ "max_visitors":  max_visitors})

  @staticmethod
  def setDeviceVisitorsNumber(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    try:
      return RESPONSE_SAMPLE.OK(DeviceController.setVistorNumber(request))
    
    except ValidationError as ve:
      return RESPONSE_SAMPLE.BAD_REQUEST({ str(ve.field): str(ve.message) })

    except Exception as e:
      print(e)
      return RESPONSE_SAMPLE.BAD_REQUEST()


  @staticmethod
  def getSingleDevice(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    return RESPONSE_SAMPLE.OK(DeviceController.getOneDevice(request))
  
  @staticmethod
  def getAllDevices(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    try:
      listOfDevices = DeviceController.getAllDevice(request)
      print(listOfDevices)
      return RESPONSE_SAMPLE.OK( data = listOfDevices )
    
    except Exception as e:
      print(e)
      return RESPONSE_SAMPLE.BAD_REQUEST()
    

  @staticmethod
  def addNewDevice(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    try:
      request.body['main_device'] = False
      print(DeviceController.addNewDevice(request))
      return RESPONSE_SAMPLE.CREATED({ 'device': 'DEVICE ADD SUCCESSFULLY' })
    
    except ValidationError as ve:
      return RESPONSE_SAMPLE.BAD_REQUEST({ str(ve.field): str(ve.message) })
    except Exception as e:
      return RESPONSE_SAMPLE.BAD_REQUEST()
    
  @staticmethod
  def getDeviceInfo(request: HTTP_REQUEST) -> HTTP_RESPONSE:
    try:
      device = DeviceController.getDeviceInstance(request)
      return RESPONSE_SAMPLE.OK({ "max_visitors": device.max_visitors })

    except Exception as e:
      print(e)
      return RESPONSE_SAMPLE.BAD_REQUEST()