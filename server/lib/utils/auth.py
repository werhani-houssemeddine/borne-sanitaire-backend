# This file will have two decorators 
# One to check authentication and other 
# to check authorization

from rest_framework.response   import Response

from lib.Http.response_samples import RESPONSE_SAMPLE
from lib.Http.headers          import RequestHeaders
from lib.token                 import Token


#? isAuthenticate is a dicorator used for secure endpoint
#? which mean endpoints need to have an authentication token
#? payload  
def isAuthenticate(callback):
  def wrapper_function(request, *args, **kwargs):
    try:

      headers    = RequestHeaders(request.headers)
      if headers.Authorization != None:
        payload = Token.getTokenPayload(headers.Authorization)
        if payload:
          return callback(request)
      
      response = RESPONSE_SAMPLE.notAuthorised()
      return Response(status = response['status_code'], data = response['body'])  
    
    except Exception as e:
      print(e)
      response = RESPONSE_SAMPLE.notAuthorised()
      return Response(status = response['status_code'], data = response['body'])

  return wrapper_function

