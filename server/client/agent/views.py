from rest_framework.decorators import api_view

from client.agent.Middleware import AgentMiddleware, RequestAgentMiddleware
from lib.make_request        import makeRequest

from lib.utils import Authenticate, Authorized

@api_view(['GET'])
def checkRequestAgent(request):
  return makeRequest(request = request, middleware = RequestAgentMiddleware.checkRequestAgent)


@api_view(['GET'])
def rejectRequestAgent(request, id):
  return makeRequest(request = request, middleware = RequestAgentMiddleware.rejectRequest, id = id)

@api_view(['POST'])
def updateAgent(request):
  return makeRequest(request = request, middleware = AgentMiddleware.updateCurrentAgent)


@api_view(['PUT'])
@Authenticate
@Authorized(['ADMIN'])
def archieveAgent(request, id):
  return makeRequest(request = request, middleware = AgentMiddleware.suspendAgent, id = id)

@api_view(['PUT'])
@Authenticate
@Authorized(['ADMIN'])
def dearchieveAgent(request, id):
  return makeRequest(request = request, middleware = AgentMiddleware.restoreAgent, id = id)

@api_view(['GET'])
@Authenticate
@Authorized(['ADMIN'])
def getAllAgents(request):
  return makeRequest(request = request, middleware = AgentMiddleware.getAllAgents)

@api_view(['GET'])
@Authenticate
@Authorized(['ADMIN'])
def getActiveAgents(request):
  return makeRequest(request = request, middleware = AgentMiddleware.getActiveAgents)

@api_view(['GET'])
@Authenticate
@Authorized(['ADMIN'])
def getArcheivedAgents(request):
  return makeRequest(request = request, middleware = AgentMiddleware.getArchivedAgents)

@api_view(['GET'])
@Authenticate
@Authorized(['ADMIN'])
def gentPendingAgents(request):
  pass

@api_view(['GET'])
@Authenticate
@Authorized(['ADMIN'])
def getOneAgentData(request, id):
  return makeRequest( 
    middleware = AgentMiddleware.getOneAgent,
    request = request, 
    id = id
  )
