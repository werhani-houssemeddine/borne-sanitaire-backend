
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

  @staticmethod
  def toJson(response_body):
    if isinstance(response_body, HTTP_RESPONSE_BODY) == False:
      raise ValueError('Only converting HTTP_RESPONSE_BODY instances')
    
    return response_body.__dict__

class HTTP_HEADER_RESPONSE:
  def __init__(self, contentType = "application/json", statusCode = 200)-> None:
    self.contentType = contentType
    self.statusCode  = statusCode


# this class will be the response returned from makeRequest function
class HTTP_RESPONSE:
  def __init__(self, body=None, headers=None):
    self.body        = body if body is not None else HTTP_RESPONSE_BODY()
    self.headers     = headers if headers is not None else HTTP_HEADER_RESPONSE()
    self.status_code = 200


  def build(self, response_data: dict) -> 'HTTP_RESPONSE':
    body_response    = response_data.get('body', {})
    headers_response = response_data.get('headers', {})

    http_header_response =HTTP_HEADER_RESPONSE(
      contentType = headers_response.get('contentType', "application/json"),
      statusCode  = headers_response.get('statusCode', 200)
    )

    self.headers     = http_header_response.contentType
    self.status_code = http_header_response.statusCode
    self.body        = HTTP_RESPONSE_BODY.build(body_response)

    return self

  def withBody(self, message = "", error = False, state = "success", data = {}):
    self.body = HTTP_RESPONSE_BODY(message, error, state, data)
    return self

  def withHeaders(self, content_type = "application/json", status_code = 200):
    self.headers = HTTP_HEADER_RESPONSE(content_type, status_code)
    return self
  
