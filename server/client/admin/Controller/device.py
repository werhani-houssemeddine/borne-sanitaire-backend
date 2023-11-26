from lib.HTTP import HTTP_REQUEST
from client.Repository import DeviceRepository 

class DeviceController:
  def checkDevice(request: HTTP_REQUEST) -> bool:
    device_id = request.query.get('device_id')
    
    if DeviceRepository.getDeviceById(device_id = device_id) == None:
      return False
    
    return True