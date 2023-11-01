from rest_framework.decorators import api_view
from rest_framework.response   import Response


from administration.authentication.Middleware import LoginMiddleware
from administration.authentication.Middleware import VerificationCodeMiddleware
from administration.authentication.Middleware import CheckVerificationCodeMiddleware

from lib import makeRequest

@api_view(['POST'])
def login(request):
  response = makeRequest(request = request, middleware = LoginMiddleware)
  return Response(status = response.status_code, data = response.body)

@api_view(['POST'])
def verify_code(request):
  response = makeRequest(request = request, middleware = VerificationCodeMiddleware)
  return Response(status = response.status_code, data = response.body)


@api_view(['GET'])
def check_verify_code(request):
  response = makeRequest(request = request, middleware = CheckVerificationCodeMiddleware)
  return Response(status = response.status_code, data = response.body)

"""
@api_view(['GET'])
def check_verify_code(request):
  try:
    email.x()
  except Exception as e:
    print(e)
  finally:
    return Response(
      status = 200, 
      data = { 'access': VerificationCodeController.handleAccessingToVerificationCode(request) }
    )
  
  """