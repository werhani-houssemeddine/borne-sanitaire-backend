from lib.HTTP     import HTTP_REQUEST, HTTP_RESPONSE

from client.authentication.Controller.Login import LoginController

# def LoginMiddleware(request: HTTP_REQUEST):
#   try:
#     (email, password) = LoginController.chekUserData(request)
#     user = LoginController.checkCredentialse(email, password)

#     if user == None: 
#       return RESPONSE_SAMPLE.NOT_AUTHORIZED()

#     token    = LoginController.generateToken(user)
#     response = LoginController.generateResponse(user, token)

#     return RESPONSE_SAMPLE.OK(response)

#   except Exception as e:
#     return RESPONSE_SAMPLE.BAD_REQUEST({ 'details': str(e) })
  

def LoginMiddleware(request: HTTP_REQUEST) -> HTTP_RESPONSE:
  LoginController