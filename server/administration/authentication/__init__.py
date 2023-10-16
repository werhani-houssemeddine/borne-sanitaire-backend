from administration.Mail import sendEmail
from administration.lib  import HTTP_REQUEST
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
          'message'    : 'Authentication done and verification code send successfully',
          'errors'     : False,
        }

    else:
      return {
        'status_code': '200',
        'errors'     : True,
        'message'    : 'Credentials are wrong'
      }
  
  except Exception as e:
    print(e)
    return {
      'status_code': 400,
      'headers'    : None,
      'message'    : str(e),
      'errors'     : True
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
        'errors'     : False,
        'body'       : {
          'message': 'Verification Code is correct',
          'token'  : 'token will be available soon ☺️'
        }
      }

    #! must add the logic of blocking users
    elif verificationCodeResponse == 'failed':
      return {
        'status_code': 200,
        'errors'     : True,
        'message'    : 'Verification Code is not correct'
      }

    else:
      return {
        'status_code': 403,
        'errors'     : True,
        'message'    : 'Blocked for providing wrong verification code more than 3 times'
      }
    
  except Exception as e:
    print(e)
    return {
      'status_code': 400,
      'headers'    : None,
      'message'    : str(e),
      'errors'     : True
    }


def CheckVerificationCodeMiddleware(request: HTTP_REQUEST):
  pass