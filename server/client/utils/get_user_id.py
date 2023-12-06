from lib.errors import ServerError
from lib.HTTP   import HTTP_REQUEST

def getUserId(request: HTTP_REQUEST) -> int:
  currentUser = request.session.get('__currentUser__')  
  if currentUser and 'id' in currentUser:
    return int(currentUser['id'])
      
  raise ServerError('USER', 'USER OR USER_ID IS MISSING IN AN AUTHORIZED ENDPOINT')