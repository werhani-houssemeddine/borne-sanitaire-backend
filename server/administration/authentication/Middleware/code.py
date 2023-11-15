from lib.Http     import HTTP_REQUEST, RESPONSE_SAMPLE
from Mail         import sendHTMLContentEmail
from Mail.samples import HTMLSample

from administration.authentication.VerificationCode import VerificationCodeController
from administration.authentication.Login            import AuthenticationController

def VerificationCodeMiddleware(request: HTTP_REQUEST):
  try:
    verificationCodeResponse = VerificationCodeController.handleCodeComparision(
      ip   = request.ip,
      code = request.body.get('verification_code')
    )

    #! must add the logic of blocking users
    if verificationCodeResponse == 'failed':
      return {
        'status_code': 200,
        'body'       : {
          'message': 'Verification Code is not correct',
          'state'  : 'failure',
          'error'  : False,
          'data'   : {
            'is_blocked': False
          }
        }
      }
    
    #? User is Blocked
    elif verificationCodeResponse == 'blocked':
      return {
        'status_code': 403,
        'body'       : {
          'message': 'Blocked for providing wrong verification code more than 3 times',
          'state'  : 'failure',
          'error'  : True,
          'data'   : {
            'is_blocked': True
          }
        }
      }

    else:
      return {
        'status_code': 200,
        'body'       : {
          'message' : 'Verification Code is correct',
          'state'   : 'success',
          'error'   : False,
          'data'    : { 
            'is_blocked': False,
            'data'      : verificationCodeResponse
          }
        }
      }
    
  except Exception as e:
    return RESPONSE_SAMPLE.badRequest({ 'details': str(e) })
  

def CheckVerificationCodeMiddleware(request: HTTP_REQUEST):
  pass