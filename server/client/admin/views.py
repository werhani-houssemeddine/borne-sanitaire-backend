from rest_framework.response   import Response
from rest_framework.decorators import api_view

from lib.make_request import makeRequest
from lib.utils        import Authenticate

from client.admin.Middleware import CurrentUser
from client.agent.Middleware import Agent


@api_view(['GET'])
@Authenticate
def currentUser(request):
    response = makeRequest(request = request, middleware = CurrentUser)
    return Response(status = 200, data = {"current-user": "houssemeddine werhani"})


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