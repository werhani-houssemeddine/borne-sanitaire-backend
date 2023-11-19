from rest_framework.response   import Response
from rest_framework.decorators import api_view

from lib.make_request import makeRequest
from lib.utils        import Authenticate

from client.agent.Middleware import Agent
from client.admin.Middleware import DeviceMiddleware


@api_view(['PUT'])
#@isAuthenticate
def edit(request):
    #response = makeRequest(request = request, middleware = SignUpController.singup)
    return Response(status = 200, data = "NOT IMPLEMENTED YET")

@api_view(['POST'])
@Authenticate
#@Authorized('ADMIN')
def addAgent(request):
    response = makeRequest(request = request, middleware = Agent.add)
    return Response(status = response.status_code, data = response.body)

@api_view(['GET'])
def checkDevice(request):
    response = makeRequest(request = request, middleware = DeviceMiddleware.checkDeviceDisponibility)
    return Response(status = response.status_code, data = response.body)