from lib.Http.http_request  import HTTP_REQUEST
from lib.Http.http_response import HTTP_RESPONSE
from lib.Http.http_response import HTTP_RESPONSE_BODY
from lib.Http.headers       import RequestHeaders

# this function will be used to make requests and will return the responses
def makeRequest(request, middleware, **args):
  try:
    ip_address = request.META.get('REMOTE_ADDR')
    headers    = RequestHeaders(request.headers)
    method     = request.method
    params     = args
    query      = request.GET.dict()
    body       = request.data
    path       = request.path
    url        = request.build_absolute_uri()
    
        
    #! add a function to get querystring parameters
    #! add args for to params

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
      url        = url
    )

    # Delete currentuser from session before sending the response 
    # to the client
    http_response = middleware(http_request)
    if "__currentUser__" in request.session.keys():
      del request.session["__currentUser__"]

    # Get the response from the middleware
    return(HTTP_RESPONSE(
      status_code = http_response['status_code'],
      headers     = None,
      body        = HTTP_RESPONSE_BODY.build(http_response['body'])
    ))

  except Exception as e:
    return HTTP_RESPONSE(
      status_code = 500,
      headers     = None,
      body        = HTTP_RESPONSE_BODY.build({
        "message" : "Internal Server Error",
        "error"   : True,
        "state"   : "failure",
        "data"    : {
          'details': str(e)
        }
      })
    )