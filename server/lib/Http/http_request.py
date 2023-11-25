# This class will create a HTTP_REQUEST we will work 
# with this request object instead of the default http.Request 
class HTTP_REQUEST:
  def __init__(self, ip_address, headers, method, params, body: dict, path, url, query, session):
    self.headers = headers
    self.method  = method
    self.params  = params
    self.query   = query 
    self.body    = body
    self.path    = path
    self.url     = url
    self.ip      = ip_address
    self.session = session