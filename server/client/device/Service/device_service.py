from requests import request

class DeviceService:
  @staticmethod
  def getCurrentVisitors(device_id):
    url = f'http://localhost:5000/device/current-device/{device_id}'
    response = request('GET', url)
    
    #? Raise error for 4xx and 5xx status code
    response.raise_for_status()

    data = response.json()
    return { 'current_visitors': data.get('current_visitors') }
  