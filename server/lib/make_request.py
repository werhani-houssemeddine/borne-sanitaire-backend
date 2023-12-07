from lib.HTTP  import HTTP_REQUEST, HTTP_RESPONSE, REQUEST_HEADERS, RESPONSE_SAMPLE

from rest_framework.response   import Response

def returnHttpResponse(http_response: HTTP_RESPONSE) -> Response:
  return Response(
    status  = http_response.status_code,
    data    = http_response.body.toJson(),
    headers = http_response.headers
  )

def makeRequest(request, middleware, **args):
  try:
    # Extract request information from the Django HTTP request
    ip_address = request.META.get('REMOTE_ADDR')
    headers    = REQUEST_HEADERS(request.headers)
    method     = request.method
    params     = args
    query      = request.GET.dict()
    body       = request.data
    path       = request.path
    url        = request.build_absolute_uri()
    session    = request.session 

    # Create a request to use send it instead of the origin request
    # send it with the middleware function (it's the api controller)
    http_request = HTTP_REQUEST( 
      ip_address = ip_address,
      headers    = headers,
      method     = method,
      params     = params,
      query      = query,
      body       = body,
      path       = path,
      url        = url,
      session    = session
    )

    #! Must called before deleting __currentUser__ from session
    http_response = middleware(http_request)

    # Delete currentuser from session before sending the response to the client
    if "__currentUser__" in request.session:
      current_user = request.session.pop("__currentUser__")
    else:
      current_user = None

    # return the response from the middleware
    # http_response: HTTP_RESPONSE = middleware(http_request)
    return returnHttpResponse(http_response) 

  except Exception as e:
    print(e)
    # Return a generic error response
    return returnHttpResponse(RESPONSE_SAMPLE.SERVER_ERROR())   
  