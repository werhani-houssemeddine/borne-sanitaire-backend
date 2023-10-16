
#! This class will be used to generate the http response
#! body to consumers
class HTTP_RESPONSE_BODY:
  pass

# this class will be the response returned from makeRequest function
class HTTP_RESPONSE:
  def __init__(self, status_code, headers, body, error = None):
    self.status_code = status_code
    self.headers     = headers
    self.body        = body
    self.error       = error

  def _addJsonHeaders(self):
    pass


# This class will create a HTTP_REQUEST we will work 
# with this request object instead of the default http.Request 
class HTTP_REQUEST:
  def __init__(self, ip_address, headers, method, params, body, path, url):
    self.headers = headers
    self.method  = method
    self.params  = params
    self.body    = body
    self.path    = path
    self.url     = url
    self.ip      = ip_address


# this function will be used to make requests and will return the responses
def makeRequest(request, middleware, **args):
  try:
    ip_address = request.META.get('REMOTE_ADDR')
    headers    = dict(request.META)
    method     = request.method
    params     = request.GET
    body       = request.data
    path       = request.path
    url        = request.build_absolute_uri()
    
        
    #! add a function to get querystring parameters
    #! add args for to params

    http_request  = HTTP_REQUEST(
      ip_address, headers, method,
      params, body, path, url
    )

    http_response = middleware(http_request)

    http_response_content = ''
    if 'body' in http_response:
      http_response_content = http_response['body']
    else:
      http_response_content = http_response['message']

    return(HTTP_RESPONSE(
      status_code = http_response['status_code'],
      headers     = None,
      body        = http_response_content,
      error       = http_response['errors']
    ))

  except Exception as e:
    #print(e)
    return HTTP_RESPONSE(
      500, 
      None, 
      { 
        'data'   : 'Internal Server Error',
        'message': str(e)
      }
    )