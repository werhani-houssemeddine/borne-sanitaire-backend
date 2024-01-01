from rest_framework.decorators import api_view

from lib.make_request                 import makeRequest
from lib.utils                        import Authenticate

from . import AgentPermessionMiddleware

@api_view(['GET'])
@Authenticate
def getPermessions(request, id):
    getAgentPermessions = AgentPermessionMiddleware.getAgentPermessions
    return makeRequest(request = request, middleware = getAgentPermessions, id = id)

@api_view(['PUT'])
@Authenticate
def setPermessions(request, id):
  setAgentPermession = AgentPermessionMiddleware.setAgentPermession
  return makeRequest(request = request, middleware = setAgentPermession, id = id)