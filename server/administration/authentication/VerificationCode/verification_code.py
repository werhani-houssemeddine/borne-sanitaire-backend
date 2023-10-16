import random
from administration.models import VerificationCode as VerificationCodeTable

class VerificationCode:

  @staticmethod
  def _generateVerificationCode(length = 8):
    listOfCharacters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    random_string = ''

    for _ in range(length):
      random_index = random.randint(0, len(listOfCharacters) - 1)
      random_string += listOfCharacters[random_index]

    return random_string
  
  # this function will save the verification code and save it
  # it will return either True or an Exception, the code will 
  # be passed as an argument 
  @staticmethod
  def _saveCode(code, ip):
    try:
      try:
        is_verification_code_exist      = VerificationCode._loadCode(ip)
        is_verification_code_exist.code = code
        
        is_verification_code_exist.save()

        return True

      except Exception as e:
        print(e)
        verificationCodeModel      = VerificationCodeTable()
        verificationCodeModel.code = code
        verificationCodeModel.ip   = ip
        
        verificationCodeModel.save()

        return True 
    
    except Exception as e:
      print(e)
      raise

  @staticmethod
  def _loadCode(ip):
    try:
      return VerificationCodeTable.objects.get(ip = ip)
        
    except Exception as e:
      raise

  #! For future versions we will add a table for blocked users
  # this method will return a boolean value 
  # it returns True if number of attempts <= 3
  @staticmethod
  def _canAcessVerificationCodePage(ip):
    return VerificationCode._loadCode(ip).number_of_attempts <= 3
