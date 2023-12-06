from rest_framework.decorators import api_view

from lib.make_request import makeRequest
from lib.utils        import Authenticate

from client.current_user.Middleware import UserMiddleware

@api_view(['PUT'])
@Authenticate
def updatePassword(request):
  return makeRequest(request = request, middleware = UserMiddleware.updatePassword)

@api_view(['PUT'])
@Authenticate
def updatePhoneNumber(request):
  return makeRequest(request = request, middleware = UserMiddleware.updatePhoneNumber)

@api_view(['PUT'])
@Authenticate
def updateUsername(request):
  return makeRequest(request = request, middleware = UserMiddleware.updateUsername)

@api_view(['POST'])
@Authenticate
def updateProfilePhoto(request):
  return makeRequest(request = request, middleware = UserMiddleware.updateProfilePhoto)