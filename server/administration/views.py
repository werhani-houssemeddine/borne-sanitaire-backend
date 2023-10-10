from rest_framework.decorators import api_view
from rest_framework.response import Response
from .authentication.login import LoginController
from .authentication.verification_code import VerificationCode
  

@api_view(['POST'])
def login(request):
  isPayloadValid = LoginController.checkPayload(request.data)

  if hasattr(isPayloadValid, 'error'):
    return Response(isPayloadValid.__dict__, status = 400)
  
  user = LoginController.verifyCredentials(isPayloadValid.email, isPayloadValid.password)

  if user.error == False:
    code = saveVerificationCode()
    sendEmail(code)
  
  return Response(user.__dict__)


def saveVerificationCode(ip):
  code = VerificationCode.generateCode()
  VerificationCode.saveCode(code = code, ip = ip)

  return code





def sendEmail(email):
  pass