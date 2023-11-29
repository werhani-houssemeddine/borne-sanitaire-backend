from rest_framework.decorators import api_view

from client.device.Middleware import DeviceMiddleware 
from lib.make_request         import makeRequest

@api_view(['GET'])
def checkDeviceAvailability(request):
  return makeRequest(request = request, middleware = DeviceMiddleware.isDeviceAvailable)

