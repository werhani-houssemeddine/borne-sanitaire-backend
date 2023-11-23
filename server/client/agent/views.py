from rest_framework.decorators import api_view
from rest_framework.response   import Response

from client.agent.Middleware import Agent
from lib.make_request        import makeRequest

@api_view(['POST'])
def addAgent(request):
  response = makeRequest(request = request, middleware = Agent.add)
  return Response(status = response.status_code, data = response.body)

@api_view(['POST'])
def editAgent(request):
  response = makeRequest(request = request, middleware = Agent.edit)
  return Response(status = response.status_code, data = response.body)


@api_view(['GET'])
def archieveAgent(request):
  response = makeRequest(request = request, middleware = Agent.archieve)
  return Response(status = response.status_code, data = response.body)

@api_view(['GET'])
def deleteAgent(request):
  response = makeRequest(request = request, middleware = Agent.delete)
  return Response(status = response.status_code, data = response.body)

@api_view(['GET'])
def checkRequestedAgent(request):
  response = makeRequest(request = request, middleware = Agent.checkRequestAgent)
  return Response(status = response.status_code, data = response.body)

@api_view(['GET'])
def rejectRequestAgent(request, id):
  response = makeRequest(request = request, middleware = Agent.rejectRequest, id = id)
  return Response(status = response.status_code, data = response.body)