from lib.errors import ValidationError
from lib.HTTP   import HTTP_REQUEST
from lib.utils      import UUID

from client.Repository import DeviceRepository

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