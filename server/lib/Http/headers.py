class RequestHeaders:
  def __init__(self, headers: dict) -> None:

    self.contentLength = headers.get('Content-Length')
    self.contentType   = headers.get('Content-Type')
    self.cookies       = headers.get('Cookie').split('; ')
    self.agent         = headers.get('User-Agent')
    self.accept        = headers.get('Accept').split(',')
    self.host          = headers.get('Host')
    