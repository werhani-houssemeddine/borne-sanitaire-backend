from administration.models import Device as DeviceTable
from django.utils          import timezone 

class DeviceRepository:
  @staticmethod
  def addDevice(device_id, user):
    try:
      device = DeviceTable.objects.get(device_id = device_id)
      device.purchase_date = timezone.now()
      device.is_saled      = True
      device.user_id       = user
      device.save()
      return device
    
    except Exception:
      raise

  @staticmethod
  def getDeviceById(device_id):
    try:
      return DeviceTable.objects.get(device_id = device_id, is_saled = False)
    except Exception:
      return None