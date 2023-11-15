from lib.Http     import HTTP_REQUEST, RESPONSE_SAMPLE
from Mail         import sendHTMLContentEmail
from Mail.samples import HTMLSample

from administration.authentication.VerificationCode import VerificationCodeController
from administration.authentication.Login            import AuthenticationController

def LoginMiddleware(request: HTTP_REQUEST) -> dict:
  try:
    user = AuthenticationController.login(request)
    
    if user != None:
      verification_code = VerificationCodeController.handeCreatingVerificationCode(user, request.ip)
      if verification_code:
        
        listOfRecipients = ['houssemwuerhani@gmail.com', 'mohamedhedigharbi101@gmail.com']
        sendHTMLContentEmail('Verification Code', verification_code, listOfRecipients, HTMLSample.VERIFICATION_CODE_SAMPLE)

        return {
          'status_code': 200,
          'body'       : {
            'message': 'Authentication done and verification code send successfully',
            'state'  : 'sucess',
            'error'  : False
          }
        }

    else:
      return {
        'status_code': 200,
        'body'       : {
            'message': 'WRONG CREDENTIALS',
            'state'  : 'Failure',
            'error'  : False
          }
      }
  
  except Exception as e:
    return RESPONSE_SAMPLE.badRequest({ 'details': str(e) })