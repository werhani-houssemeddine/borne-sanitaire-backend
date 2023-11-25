from lib.HTTP import HTTP_REQUEST, RESPONSE_SAMPLE

from .signup import SignupAdminMiddleware
from .signup import SignupAgentMiddleware

def SignupMiddleware(request: HTTP_REQUEST):
  device_id = request.query.get('device')
  agent_id  = request.query.get('agent')

  if device_id == None and agent_id == None:
    return RESPONSE_SAMPLE.NOT_FOUND()

  if device_id != None:
    return SignupAdminMiddleware(request)

  if agent_id != None:
    return SignupAgentMiddleware(request)