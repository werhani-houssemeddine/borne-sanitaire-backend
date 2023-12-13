from rest_framework.decorators import api_view

from lib.make_request                 import makeRequest
from lib.utils                        import Authenticate

from client.authentication import CurrentUserMiddleware
from client.authentication import SignupMiddleware
from client.authentication import LoginMiddleware


@api_view(['POST'])
@Authenticate
def enableOTP(request):
    return makeRequest(request = request, middleware = LoginMiddleware)


@api_view(['POST'])
@Authenticate
def disableOTP(request):
    return makeRequest(request = request, middleware = SignupMiddleware)

@api_view(['GET'])
@Authenticate
def checkOTP(request):
    return makeRequest(request = request, middleware = CurrentUserMiddleware)
