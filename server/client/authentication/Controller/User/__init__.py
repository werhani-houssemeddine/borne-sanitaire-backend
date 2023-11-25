from lib.HTTP.headers import RequestHeaders
from lib.HTTP         import HTTP_REQUEST
from lib.token        import Token

def getToken(headers: RequestHeaders) -> str:
  return headers.Authorization

#? This controller will just return the user info
#? the controller doesn't need to validate the token
#? because the token will already checked with the decorator @Authenticate
#? for better inforamtion just check lib.utils.auth
#? the data comming to this controller is valid also we are sure 
#? that the request have headers property which is also have Authorization property

#! For future version we may add a singelton instance and pass it in @Authenticate

class CurrentUserController:
  def getUser(request: HTTP_REQUEST):
    token = getToken(request.headers)
    payload_token = Token.getTokenPayload(token)
    
    return {
      'id': payload_token['id'],
      'user': {
        'username': payload_token['username'],
        'email'   : payload_token['email'],
        'role'    : payload_token['role']
      }  
    }
