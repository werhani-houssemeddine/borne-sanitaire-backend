from rest_framework.decorators import api_view

from lib.make_request                 import makeRequest
from lib.utils                        import Authenticate

from client.authentication.Middleware import DeleteAccountMiddleware, SignupEmailAdmin
from client.authentication.Middleware import LoginMiddlewareOTPVerification, OTPMiddleware


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

@api_view(['POST'])
def signupEmail(request):
    return makeRequest(request = request, middleware = SignupEmailAdmin)

@api_view(['POST'])
def checkSignupCode(request):
    return makeRequest(request = request, middleware = OTPMiddleware.compareOTP)

@api_view(['POST'])
def checkLoginCode(request):
    return makeRequest(request = request, middleware = LoginMiddlewareOTPVerification)