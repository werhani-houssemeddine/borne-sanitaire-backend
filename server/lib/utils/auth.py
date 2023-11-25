# This file will have two decorators 
# One to check authentication and other 
# to check authorization

from rest_framework.response   import Response

from lib.HTTP.response_samples import RESPONSE_SAMPLE
from lib.HTTP.headers          import REQUEST_HEADERS
from lib.token                 import Token

from client.Repository         import User as UserRepository

from client.utils import CurrentUser

#? isAuthenticate is a dicorator used for secure endpoint
#? which mean endpoints need to have an authentication token
#? payload  
def isAuthenticate(callback):
  def wrapper_function(request, *args, **kwargs):
    try:

      headers    = REQUEST_HEADERS(request.headers)
      if headers.Authorization != None:
        payload = Token.getTokenPayload(headers.Authorization)
        if payload:

          #? The user data object will have the current user
          #? such as role email and id
          email = payload.get('email')
          id    = payload.get('id')

          if email == None or id == None:
            return Response(status = 403, data = { 'message': 'an error occuring while processing your data' })

          #? this payload refers to super admin
          if payload.get('super_admin') == True:
            request.session['__currentUser__'] = payload

          else:
            #? Get user object            
            client = UserRepository.getUserByEmail(email)

            #? check for client role, if it's AGENT we have to add 
            #? the permissions
            if client.role == "ADMIN":
              request.session['__currentUser__'] = CurrentUser(email, client.user_name, id, client.role).__dict__
            else: 
              #! If userData['role'] == AGENT
              #! We Have to check the permission table
              pass

          
          return callback(request, *args, **kwargs)
      
      raise Exception()  
    
    except Exception as e:
      response = RESPONSE_SAMPLE.notAuthorised()
      return Response(status = response['status_code'], data = response['body'])

  return wrapper_function


def AdminAuthenticate(callback):
  def wrapper_function(request, *args, **kwargs):
    try:
      headers    = REQUEST_HEADERS(request.headers)
      if headers.Authorization != None:
        payload = Token.getTokenPayload(headers.Authorization)
        if payload:
          #? The user data object will have the current user
          #? such as role email and id
          email = payload.get('email')
          id    = payload.get('id')

          if email == None or id == None:
            return Response(status = 403, data = { 'message': 'an error occuring while processing your data' })
          
          if payload.get('super_admin') == True:
            request.session['__currentUser__'] = payload
            
            return callback(request)
        
        raise Exception()
            
    
    except Exception as e:
      print(e)
      response = RESPONSE_SAMPLE.notAuthorised()
      return Response(status = response['status_code'], data = response['body'])

  return wrapper_function


def isAuthorized(permission):
  def decorator_function(callback):
    def wrapper_function(request, *args, **kwargs):
      try:
        currentUserData: CurrentUser = request.session.get('__currentUser__')

        if currentUserData == None:
          raise Exception()

        role = currentUserData['role']
        if role == 'ADMIN':
            return callback(request, *args, **kwargs)
        else:
          if role == permission:
            return callback(request, *args, **kwargs)

        raise Exception()  

      except Exception as e:
        response = RESPONSE_SAMPLE.notAuthorised()
        return Response(status = response['status_code'], data = response['body'])

    return wrapper_function
  return decorator_function
