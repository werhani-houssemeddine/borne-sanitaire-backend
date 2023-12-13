from rest_framework.decorators import api_view

from lib.make_request                 import makeRequest
from lib.utils                        import Authenticate

from client.authentication.Middleware import OTPMiddleware, DeleteAccountMiddleware


@api_view(['POST'])
@Authenticate
def enableOTP(request):
    return makeRequest(request = request, middleware = OTPMiddleware.enableOTP)


@api_view(['POST'])
@Authenticate
def disableOTP(request):
    return makeRequest(request = request, middleware = OTPMiddleware.disableOTP)

@api_view(['GET'])
@Authenticate
def checkOTP(request):
    return makeRequest(request = request, middleware = OTPMiddleware.checkOTP)

@api_view(['DELETE'])
@Authenticate
def deleteAccount(request):
    return makeRequest(request = request, middleware = DeleteAccountMiddleware)