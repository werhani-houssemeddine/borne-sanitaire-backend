from lib.errors import ValidationError
from lib.HTTP   import HTTP_REQUEST
from lib.utils  import UUID

from administration.models import Device as DeviceModel
from client.Repository     import DeviceRepository, UserRepository

from client.utils import getUserId

from client.device.Service import DeviceService

class DeviceController:
  @staticmethod
  def checkDeviceId(uuid_str):
    return UUID.validateUUID(uuid_str)
  
  @staticmethod
  def isDeviceAvailable(request: HTTP_REQUEST) -> True:
    try:
      device_id = DeviceController.checkDeviceId(request.query.get('device_id'))
      device    = DeviceRepository.getNonSelledDevice(device_id)
      
      return True
    
    except ValidationError as e: raise
    except Exception as e: raise

  @staticmethod
  def getDeviceInstance(request: HTTP_REQUEST) -> DeviceModel:
    try:
      device_id = DeviceController.checkDeviceId(request.params.get('device'))
      return DeviceRepository.getDevice(device_id)

    except ValidationError as e: raise
    except Exception as e: raise

  
  @staticmethod
  def getOneDevice(request: HTTP_REQUEST):
    try:
      device = DeviceController.getDeviceInstance(request)
      
      if device.user_id.id == getUserId(request):
        return DeviceController.formatDeviceResponse(device)

      raise ValidationError('UNATHORIZED', 'DEVICE ID')      

    except ValidationError as e: raise
    except Exception as e: raise

  
  @staticmethod
  def getVistorNumber(request: HTTP_REQUEST) -> int | None:
    try:
      device  = DeviceController.getDeviceInstance(request)
      user_id = getUserId(request)

      if device.user_id.id == user_id:
        return device.max_visitors
    
    except ValidationError as e: raise
    except Exception as e: raise

  
  @staticmethod
  def setVistorNumber(request: HTTP_REQUEST):
    try:
      max_visitors = request.body.get('max_visitors')
      if max_visitors != None:
        device = DeviceController.getDeviceInstance(request)
        
        if int(max_visitors) >= 0:
          
          serviceResponse  = DeviceService.getCurrentVisitors(device_id = device.device_id)
          current_visitors = serviceResponse.get('current_visitors')

          if current_visitors != None:
            if current_visitors < int(max_visitors):
             
              device.max_visitors = int(max_visitors)
              device.save()
              return int(max_visitors)

            raise ValidationError('invalid number', 'Visitors number already bigger than the value provided') 
      
      raise ValidationError('update visitors', 'Invalid visitors number')
      
    except ValidationError as e: raise
    except Exception as e: raise


  @staticmethod
  def getAllDevice(request: HTTP_REQUEST):
    try:
      user_id = getUserId(request)
      user    = UserRepository.getUserById(user_id)
      
      if user.role == "AGENT": raise ValidationError("UNAUTHORIZED", "CANNOT ACCESS THIS ENDPOINT")

      listOfDevices = DeviceRepository.getAllDevices(user_id)

      return list(
        map(DeviceController.formatDeviceResponse, listOfDevices)
      )
    
    except ValidationError: raise 
    except Exception: raise

  @staticmethod
  def formatDeviceResponse(device: DeviceModel) -> dict:
    return {
      'purchase_date': device.purchase_date,
      'max_visitors' : device.max_visitors,
      'user_id'      : device.user_id.id,
      'version'      : device.version,
      'title'        : device.title,
      'id'           : device.device_id,

      'main'         : device.main
    }
  
  @staticmethod
  def addNewDevice(request: HTTP_REQUEST):
    try:
      device_id = request.body.get('device_id')
      device    = DeviceRepository.addDevice(
        device_id   = device_id, 
        user        = UserRepository.getUserById(getUserId(request)),
        main_device = False
      )

      return DeviceController.formatDeviceResponse(device)
    
    except ValidationError:
      raise 
    except Exception:
      raise