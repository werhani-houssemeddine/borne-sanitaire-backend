from lib.Http     import HTTP_REQUEST, RESPONSE_SAMPLE
from client.authentication.Controller.User import CurrentUserController

def CurrentUserMiddleware(request: HTTP_REQUEST):
  try:
    print(request.headers)

  except Exception as e:
    return RESPONSE_SAMPLE.badRequest({ 'details': str(e) })