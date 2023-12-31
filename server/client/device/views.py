from rest_framework.decorators import api_view

from client.device.Middleware import DeviceMiddleware 
from lib.make_request         import makeRequest

from lib.utils import Authenticate

@api_view(['GET'])
def checkDeviceAvailability(request):
  return makeRequest(request = request, middleware = DeviceMiddleware.isDeviceAvailable)


@api_view(['GET', 'PUT'])
@Authenticate
def visitors(request, device):
  makeCustomMakeRequest = lambda middleware: makeRequest(
    request = request, 
    middleware = middleware, 
    device = device
  )

  if request.method == "GET":
    return makeCustomMakeRequest(middleware = DeviceMiddleware.getDeviceVisitorsNumber)
  elif request.method == "PUT":
    return makeCustomMakeRequest(middleware = DeviceMiddleware.setDeviceVisitorsNumber)
  
 
@api_view(['GET'])
@Authenticate
def getOneDevice(request, device):
  return makeRequest(
    request = request, 
    middleware = DeviceMiddleware.getSingleDevice, 
    device = device
  )

@api_view(['GET'])
@Authenticate
def getAllDevices(request):
  return makeRequest(request = request, middleware = DeviceMiddleware.getAllDevices)

@api_view(['POST'])
@Authenticate
def addNewDevice(request):
  return makeRequest(request = request, middleware = DeviceMiddleware.addNewDevice)


#? This endpoint is mainly used in the real-time server 
#? no authentication nedded and he only return the max_visitor_number
@api_view(['GET'])
def getDeviceInfo(request, device):
  return makeRequest(request = request, middleware = DeviceMiddleware.getDeviceInfo, device = device)