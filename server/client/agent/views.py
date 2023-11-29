from rest_framework.decorators import api_view

from client.agent.Middleware import AgentMiddleware, RequestAgentMiddleware
from lib.make_request        import makeRequest

@api_view(['GET'])
def checkRequestAgent(request, id):
  return makeRequest(request = request, middleware = RequestAgentMiddleware.checkRequestAgent, id = id)


@api_view(['GET'])
def rejectRequestAgent(request, id):
  return makeRequest(request = request, middleware = RequestAgentMiddleware.rejectRequest, id = id)

@api_view(['POST'])
def updateAgent(request):
  return makeRequest(request = request, middleware = AgentMiddleware.updateCurrentAgent)


@api_view(['GET'])
def archieveAgent(request):
  return makeRequest(request = request, middleware = AgentMiddleware.suspendCurrentAgent)

@api_view(['GET'])
def getAllAgents(request):
  pass

@api_view(['GET'])
def getActiveAgents(request):
  pass

@api_view(['GET'])
def getArcheivedAgents(request):
  pass

@api_view(['GET'])
def gentPendingAgents(request):
  pass

@api_view
def getOneAgentData(request, id):
  pass