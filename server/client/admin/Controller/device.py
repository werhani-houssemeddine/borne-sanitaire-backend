from lib.Http import HTTP_REQUEST
from client.Repository import Device as DeviceTable

class DeviceController:
  def checkDevice(request: HTTP_REQUEST) -> bool:
    device_id = request.query.get('device')
    
    if DeviceTable.getDeviceById(device_id = device_id) == None:
      return False
    
    return True