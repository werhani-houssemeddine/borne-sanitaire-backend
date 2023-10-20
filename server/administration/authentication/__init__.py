from lib.Http.http_request import HTTP_REQUEST
from Mail                import sendEmail
from .VerificationCode   import VerificationCodeController
from .Login              import AuthenticationController


def LoginMiddleware(request: HTTP_REQUEST):
  try:
    if AuthenticationController.login(request):
      verification_code = VerificationCodeController.handeCreatingVerificationCode(request.ip);
      if verification_code:
        # print ("Verification Code created successfully", verification_code)
        listOfRecipients = ['houssemwuerhani@gmail.com', 'mohamedhedigharbi101@gmail.com']
        sendEmail('Verification Code', verification_code, listOfRecipients)

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
            'message': 'Credentials are wrong',
            'state'  : 'Failure',
            'error'  : True
          }
      }
  
  except Exception as e:
    print(e)
    return {
      'status_code': 400,
      'body'       : {
        'message' : 'Bad Request',
        'state'   : 'failure',
        'error'   : True,
        'data'    : { 
          'details': str(e) 
        }
      }
    }


def VerificationCodeMiddleware(request: HTTP_REQUEST):
  try:
    verificationCodeResponse =VerificationCodeController.handleCodeComparision(
      ip   = request.ip,
      code = request.body.get('verification_code')
    )

    if verificationCodeResponse == 'success':
      return {
        'status_code': 200,
        'body'       : {
          'message' : 'Verification Code is correct',
          'state'   : 'sucess',
          'error'   : False,
          'data'    : { 
            'is_blocked': False,
            'token'     : 'token will be available soon ☺️',
          }
        }
      }

    #! must add the logic of blocking users
    elif verificationCodeResponse == 'failed':
      return {
        'status_code': 200,
        'body'       : {
          'message': 'Verification Code is not correct',
          'state'  : 'failure',
          'error'  : True,
          'data'   : {
            'is_blocked': False
          }
        }
      }

    else:
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
    
  except Exception as e:
    print(e)
    return {
      'status_code': 400,
      'body'       : {
        'message' : 'Bad Request',
        'state'   : 'failure',
        'error'   : True,
        'data'    : { 
          'details': str(e) 
        }
      }
    }


def CheckVerificationCodeMiddleware(request: HTTP_REQUEST):
  pass