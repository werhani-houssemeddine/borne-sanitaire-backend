from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import AccountSerializer
from rest_framework import status 
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from client.authentication.Signup import SignUpController
from client.authentication.Login  import LoginController
from lib.make_request             import makeRequest
from lib.token                    import Token  


# from ..lib import makeRequest

@api_view(['GET'])
def currentUser(request):
    token = request.headers['Authorization']
    if(token == None):
        return Response({ 'token': 'Not Found' }, status = 401)
    else:
        try:
            

            payload = {
                "email": "houssemwuerhani@gmail.com",
                "password": "123456789",
                "id": 1
            }

            jwt_token = Token.createToken(payload)
            
            return Response({ 'token': jwt_token })
        
        except Exception as e:
            print(f"Exception {e}")
            return Response({ 'token': None }, status = 401)
        

@api_view(['POST'])
def login(request):
    response = makeRequest(request = request, middleware = LoginController.login)
    return Response(status = response.status_code, data = response.body)


@api_view(['POST'])
def signup(request):
    response = makeRequest(request = request, middleware = SignUpController.singup)
    return Response(status = response.status_code, data = response.body)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed for {}".format(request))



