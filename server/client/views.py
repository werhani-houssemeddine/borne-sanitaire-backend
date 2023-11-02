from rest_framework.response   import Response
from rest_framework.decorators import api_view

from client.authentication.Middleware import LoginMiddleware
from client.authentication.Middleware import SignupAdminMiddleware
from lib.make_request                 import makeRequest

@api_view(['POST'])
def login(request):
    response = makeRequest(request = request, middleware = LoginMiddleware)
    return Response(status = response.status_code, data = response.body)


@api_view(['POST'])
def signup(request):
    response = makeRequest(request = request, middleware = SignupAdminMiddleware)
    return Response(status = response.status_code, data = response.body)
