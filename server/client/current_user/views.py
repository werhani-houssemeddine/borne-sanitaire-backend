from rest_framework.decorators import api_view

from lib.make_request import makeRequest
from lib.utils        import Authenticate

from client.current_user.Middleware import UserMiddleware

@api_view(['GET'])
@Authenticate
def current(request):
  return makeRequest(request = request, middleware = UserMiddleware.getCurrentUser)
  

@api_view(['PUT'])
def update(request):
  pass

@api_view(['GET'])
def archeive(request):
  pass