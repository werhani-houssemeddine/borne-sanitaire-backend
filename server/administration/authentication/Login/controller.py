from lib.Http.http_request import HTTP_REQUEST
from .business_logic    import LoginBusinessLayer
from lib.token import Token
    
class AuthenticationController:
  @staticmethod 
  def login(request: HTTP_REQUEST):
    try:
      data = request.body

      (email, password) = LoginBusinessLayer.validate_login_data(
        password = data.get('password'),
        email    = data.get('email')
      )
      checkingResult = LoginBusinessLayer.check_credentials(email, password)
      
      if checkingResult != None:
        user = checkingResult
        payload = { 'email': user.email, 'username': user.username, 'phone_number': user.phone_number }
        payload['token'] = Token.createToken(payload)

        return payload
      
      return None
        

    except Exception as e:
      raise
  
