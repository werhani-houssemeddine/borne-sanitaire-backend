from lib.errors import ValidationError

from client.models import OTP_Model

import random

class OTP_Repository:
  @staticmethod
  def getOTPCode(email):
    try:
      return OTP_Model.objects.get(email = email)
    
    except OTP_Model.DoesNotExist: return None    
    except Exception: raise

  @staticmethod
  def createNewOTP(email):
    isEmailExist = OTP_Repository.getOTPCode(email)
    code = random.randint(100000, 999999)

    if isEmailExist != None:
      isEmailExist.delete()
    
    newOTP = OTP_Model.objects.create(email = email, code = code)
    newOTP.save()
    return code

  @staticmethod
  def compareOTP(email, code):
    isOTPExist = OTP_Repository.getOTPCode(email)
    
    if isOTPExist == None: raise ValidationError('code', 'expired or invalid code')
        
    return isOTPExist.code == code

  @staticmethod
  def deleteOTP(email):
    isOTPExist = OTP_Repository.getOTPCode(email)
    if isOTPExist == None: raise ValidationError('code', 'expired or invalid code')

    isOTPExist.delete()
