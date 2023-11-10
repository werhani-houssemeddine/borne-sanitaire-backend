from rest_framework.response   import Response
from rest_framework.decorators import api_view

from lib.make_request                 import makeRequest
from lib.utils                        import Authenticate

from client.authentication import CurrentUserMiddleware
from client.authentication import SignupMiddleware
from client.authentication import LoginMiddleware


@api_view(['POST'])
def login(request):
    response = makeRequest(request = request, middleware = LoginMiddleware)
    return Response(status = response.status_code, data = response.body)


@api_view(['POST'])
def signup(request):
    response = makeRequest(request = request, middleware = SignupMiddleware)
    return Response(status = response.status_code, data = response.body)

@api_view(['GET'])
@Authenticate
def currentUser(request):
    response = makeRequest(request = request, middleware = CurrentUserMiddleware)
    return Response(status = 200, data = {"current-user": "houssemeddine werhani"})
