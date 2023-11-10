from lib.Http import HTTP_REQUEST, RESPONSE_SAMPLE

from .signup_admin import SignupAdminMiddleware
from .signup_agent import SignupAgentMiddleware

def SignupMiddleware(request: HTTP_REQUEST):
  device_id = request.query.get('device')
  agent_id  = request.query.get('agent')

  if device_id == None and agent_id == None:
    return RESPONSE_SAMPLE.notFound()

  if device_id != None:
    return SignupAdminMiddleware(request)

  if agent_id != None:
    return SignupAgentMiddleware(request)