from .verification_code import VerificationCode

#? Need to move to another module
class InvalidInputException(Exception):
  pass


class VerificationCodeController:
  @staticmethod
  def handleCodeComparision(ip, code):
    if code is None:
      raise InvalidInputException('Verification code is required')

    loadCodeFromDataBase = VerificationCode._loadCode(ip)
    getUserCode          = code

    if(getUserCode == loadCodeFromDataBase.code):
      loadCodeFromDataBase.delete()
      return 'success'

    else:
      nb_attempts = loadCodeFromDataBase.number_of_attempts

      loadCodeFromDataBase.number_of_attempts = nb_attempts + 1
      loadCodeFromDataBase.save()

      return 'blocked' if nb_attempts > 3 else 'failed'
    
  
  # This method will create and save the verification code
  @staticmethod
  def handeCreatingVerificationCode(ip):
    try:
      code = VerificationCode._generateVerificationCode(),
      code = code[0]
      VerificationCode._saveCode( code = code, ip = ip )
      return code
    
    except Exception as e:
      raise
 
  #! This method need to use other method for blocking access [using cookies]
  # this method will call canAccessVerificationCodePage from VerificationCode class
  # ans return a boolean indicating whether the visitor is allowed to access the 
  # page using the ip address 
  @staticmethod
  def handleAccessingToVerificationCode(ip):
    try:
      return VerificationCode._canAcessVerificationCodePage(ip)
    except Exception as e:
      print(e)
      raise Exception