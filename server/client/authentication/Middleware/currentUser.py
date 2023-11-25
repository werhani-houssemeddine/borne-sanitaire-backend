from lib.HTTP     import HTTP_REQUEST, RESPONSE_SAMPLE
from client.authentication.Controller.User import CurrentUserController

def CurrentUserMiddleware(request: HTTP_REQUEST):
  try:
    #
      # No need to check if the user == None because 
      # we are too sure that the response is valid
      # check the controller for more information
    #

    return RESPONSE_SAMPLE.ok(CurrentUserController.getUser(request))
    
  except Exception as e:
    return RESPONSE_SAMPLE.badRequest({ 'details': str(e) })