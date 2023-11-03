class RequestHeaders:
  def __init__(self, headers: dict) -> None:
    self.contentLength = headers.get('Content-Length')
    self.contentType   = headers.get('Content-Type')
    self.agent         = headers.get('User-Agent')
    self.host          = headers.get('Host')
    self.Authorization = headers.get('Authorization')
    
    self.__getCookies(headers)
    self.__getAccept(headers)

  # Not all HTTP Request have cookies, we need to check
  # the presence of them before split or making other operations
  def __getCookies(self, headers):
    if isinstance(headers.get('Cookie'), str):
      self.cookies = headers.get('Cookie').split('; ')
    else:
      self.cookies = None

  # The same reason as Cookies
  def __getAccept(self, headers):
    if isinstance(headers.get('Cookie'), str):
      self.accept = headers.get('Accept').split(',')
    else:
      self.accept = None    
