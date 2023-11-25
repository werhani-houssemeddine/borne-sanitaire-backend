from lib.HTTP.http_request  import HTTP_REQUEST
from lib.HTTP.http_response import HTTP_RESPONSE
from lib.HTTP.headers       import RequestHeaders

def makeRequest(request, middleware, **args):
  try:
    # Extract request information from the Django HTTP request
    ip_address = request.META.get('REMOTE_ADDR')
    headers    = RequestHeaders(request.headers)
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

    # Delete currentuser from session before sending the response to the client
    http_response: HTTP_RESPONSE = middleware(http_request)
    if "__currentUser__" in request.session:
      current_user = request.session.pop("__currentUser__")
    else:
      current_user = None

    # Get the response from the middleware
    return HTTP_RESPONSE(
      status_code = http_response.status_code,
      headers     = None,
      body        = http_response.body
    )

  except Exception as e:

    # Return a generic error response
    return HTTP_RESPONSE().withBody(
      message = "INTERNAL SERVER ERROR",
      error   = True,
      state   = "FAILURE"  
    ).withStatus(500).withHeaders()
    
  