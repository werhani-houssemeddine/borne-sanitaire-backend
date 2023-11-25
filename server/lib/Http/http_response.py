
#! This class will be used to generate the http response
#! body to consumers
class HTTP_RESPONSE_BODY:
  def __init__(self, message = "", error = False, state = "success", data = {}) -> None:
    self.message = message
    self.error   = error
    self.state   = state
    self.data    = data

  @classmethod
  def build(cls, body_response: dict) -> 'HTTP_RESPONSE_BODY':
    response = cls()

    response.message = body_response.get('message', response.message)
    response.error   = body_response.get('error', response.error)
    response.state   = body_response.get('state', response.state).upper()

    if response.state not in {'SUCCESS', 'FAILURE'}:
      response.state = 'SUCCESS'

    response.data = body_response.get('data', response.data)

    return response


  def toJson(self) -> dict:
    return self.__dict__

class HTTP_HEADER_RESPONSE:
  def __init__(self, contentType = "application/json")-> None:
    self.contentType = contentType


# this class will be the response returned from makeRequest function
class HTTP_RESPONSE:
  def __init__(self, body = None, headers = None, status_code = 200):
    self.body        = body if body is not None else HTTP_RESPONSE_BODY()
    self.headers     = headers if headers is not None else HTTP_HEADER_RESPONSE()
    self.status_code = 200

  def withBody(self, message = "", error = False, state = "success", data = {}):
    self.body = HTTP_RESPONSE_BODY(message, error, state, data)
    return self

  def withHeaders(self, content_type = "application/json"):
    self.headers = HTTP_HEADER_RESPONSE(content_type)
    return self
  
  def withStatus(self, status_code = 200):
    self.status_code = status_code
    return self
  
