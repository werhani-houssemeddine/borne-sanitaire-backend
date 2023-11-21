from .verification_code import VerificationCode
from lib.token import Token
from administration.models import SuperAdmin as SuperAdminTable


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

      #? Payload a dictionary { 'email', 'username', 'phone_number' }
      payload = Token.getTokenPayload(loadCodeFromDataBase.token)
      
      #? Add token to payload
      payload['token'] = loadCodeFromDataBase.token

      #? Delete verification code
      loadCodeFromDataBase.delete()

      #? return value { 'email', 'username', 'phone_number', 'token' }
      return payload

    else:
      nb_attempts = loadCodeFromDataBase.number_of_attempts

      loadCodeFromDataBase.number_of_attempts = nb_attempts + 1
      loadCodeFromDataBase.save()

      return 'blocked' if nb_attempts >= 3 else 'failed'
    
  
  # This method will create and save the verification code
  @staticmethod
  def handeCreatingVerificationCode(user: SuperAdminTable, ip):
    try:
      token = Token.createToken({
        'email': user.email, 
        'username': user.username, 
        'phone_number': user.phone_number,
        'super_admin' : True,
        'id': user.id
      })

      token = token.decode('utf-8')

      code = VerificationCode._generateVerificationCode(),
      code = code[0]
      VerificationCode._saveCode( code = code, ip = ip, token = token )
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
