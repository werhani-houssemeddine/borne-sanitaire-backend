from rest_framework.response   import Response
from rest_framework.decorators import api_view

from client.authentication.Signup import SignUpController
from client.authentication.Login  import LoginController
from lib.make_request             import makeRequest
from lib.token                    import Token  


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
