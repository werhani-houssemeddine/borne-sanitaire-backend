from rest_framework.response   import Response
from rest_framework.decorators import api_view

from lib.make_request             import makeRequest
     

@api_view(['GET'])
#@isAuthenticate
def currentUser(request):
    #response = makeRequest(request = request, middleware = LoginController.login)
    return Response(status = 200, data = {"current-user": "houssemeddine werhani"})


@api_view(['PUT'])
#@isAuthenticate
def edit(request):
    #response = makeRequest(request = request, middleware = SignUpController.singup)
    return Response(status = 200, data = "NOT IMPLEMENTED YET")
