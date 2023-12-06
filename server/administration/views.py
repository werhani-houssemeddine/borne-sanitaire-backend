from rest_framework.decorators import api_view
from rest_framework.response   import Response

import qrcode
from io import BytesIO
from django.http import HttpResponse

from administration.authentication.Middleware import LoginMiddleware
from administration.authentication.Middleware import VerificationCodeMiddleware
from administration.authentication.Middleware import CheckVerificationCodeMiddleware

from administration.account.Middleware import UpdateSuperAdminMiddleware 

from administration.models import Device

from lib.make_request import makeRequest
from lib.utils        import Authenticate

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

#! This endpoint is for testing purpose
@api_view(['GET'])
def addDevice(request):
  d = Device(version = "1.0.0")
  d.save()

  qr = qrcode.QRCode(
      version=1,
      error_correction=qrcode.constants.ERROR_CORRECT_L,
      box_size=10,
      border=4,
  )

  qr.add_data(str(d.device_id))
  qr.make(fit=True)

  img = qr.make_image(fill_color="black", back_color="white")
  buffer = BytesIO()
  img.save(buffer)
  buffer.seek(0)

  # Return the image as a Django HttpResponse
  return HttpResponse(buffer.read(), content_type="image/png")
  # return Response(status = 201, data = str(d.device_id))

@api_view(['PUT'])
@Authenticate
def editSuperAdmin(request):
  response = makeRequest(request = request, middleware = UpdateSuperAdminMiddleware)
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