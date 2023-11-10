from lib.Http     import HTTP_REQUEST, RESPONSE_SAMPLE

from client.authentication.Controller.Login import LoginController

def LoginMiddleware(request: HTTP_REQUEST):
  try:
    (email, password) = LoginController.chekUserData(request)
    user = LoginController.checkCredentialse(email, password)

    if user == None: 
      return RESPONSE_SAMPLE.notAuthorised()

    token    = LoginController.generateToken(user)
    response = LoginController.generateResponse(user, token)

    return RESPONSE_SAMPLE.ok(response)

  except Exception as e:
    return RESPONSE_SAMPLE.badRequest({ 'details': str(e) })