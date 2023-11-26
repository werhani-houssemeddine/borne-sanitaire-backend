from rest_framework.response   import Response
from rest_framework.decorators import api_view

from lib.make_request import makeRequest
from lib.utils        import Authenticate, Authorized

from client.admin.Middleware import DeviceMiddleware
from client.admin.Middleware import RequestAgentAdminMiddleware

@api_view(['PUT'])
#@isAuthenticate
def edit(request):
    #response = makeRequest(request = request, middleware = SignUpController.singup)
    return Response(status = 200, data = "NOT IMPLEMENTED YET")

@api_view(['POST'])
@Authenticate
@Authorized('ADMIN')
def addAgent(request):
    return makeRequest(request = request, middleware = RequestAgentAdminMiddleware.sendNewRequest)

@api_view(['GET'])
def checkDevice(request):
    response = makeRequest(request = request, middleware = DeviceMiddleware.checkDeviceDisponibility)
    return Response(status = response.status_code, data = response.body)

@api_view(['DELETE'])
@Authenticate
@Authorized('ADMIN')
def deleteRequestAgent(request, id):
    return makeRequest(request = request, middleware = RequestAgentAdminMiddleware.deleteRequest, id = id)

@api_view(['GET'])
@Authenticate
@Authorized('ADMIN')
def getSingleRequestAgent(request, id):
    return makeRequest(request = request, middleware = RequestAgentAdminMiddleware.getOneRequest, id = id)

@api_view(['GET'])
@Authenticate
@Authorized('ADMIN')
def getAllRequestAgent(request):
    return makeRequest(request = request, middleware = RequestAgentAdminMiddleware.getAllRequest)
