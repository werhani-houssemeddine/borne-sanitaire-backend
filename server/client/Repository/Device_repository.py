from lib.errors import ValidationError

from administration.models import Device as DeviceTable
from django.utils          import timezone 


class DeviceRepository:
  @staticmethod
  def addDevice(device_id, user):
    try:
      device = DeviceTable.objects.get(device_id = device_id, is_saled = False)
      device.purchase_date = timezone.now()
      device.is_saled      = True
      device.user_id       = user
      device.save()
      return device
    
    except DeviceTable.DoesNotExist:
      raise ValidationError('DEVICE', 'EXPIRED DEVICE') 

    except Exception:
      raise

  @staticmethod
  def getNonSelledDevice(device_id) -> DeviceTable:
    try:
      return DeviceTable.objects.get(device_id = device_id, is_saled = False)
    
    except DeviceTable.DoesNotExist as e:
      raise ValidationError('device', 'DEVICE DOES NOT EXIST')
    except Exception as e:
      raise

  @staticmethod
  def getDevice(device_id):
    try:
      return DeviceTable.objects.get(device_id = device_id, is_saled = True)

    except DeviceTable.DoesNotExist as e:
      raise ValidationError('device', 'DEVICE DOES NOT EXIST')
    except Exception as e:
      raise
  
  @staticmethod
  def getAllDevices(user_id):
    try:
      return DeviceTable.objects.filter(user_id = user_id)
    
    except DeviceTable.DoesNotExist:
      return None
    
    except Exception as e: 
      print(e)
      raise