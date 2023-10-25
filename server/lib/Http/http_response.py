
#! This class will be used to generate the http response
#! body to consumers
class HTTP_RESPONSE_BODY:
  def __init__(self, message = "", error = False, state = "success", data = {}) -> None:
    self.message = message
    self.error   = error
    self.state   = state
    self.data    = data

  @staticmethod
  def build(body_response: dict):
    response = HTTP_RESPONSE_BODY()

    if 'message' in body_response:
      response.message = body_response['message']

    if 'error' in body_response:
      if isinstance(body_response['error'], bool):
        response.error = body_response['error']

    if 'state' in body_response:
      state = body_response['state'].upper()
      if state == 'SUCCESS' or state == 'FAILURE':
        response.state = state

    if 'data' in body_response:
      response.data = body_response['data']
    else:
      response.__delattr__('data')

    return response

  @staticmethod
  def toJson(response_body):
    if isinstance(response_body, HTTP_RESPONSE_BODY) == False:
      raise ValueError('Only converting HTTP_RESPONSE_BODY instances')
    
    return response_body.__dict__


# this class will be the response returned from makeRequest function
class HTTP_RESPONSE:
  def __init__(self, status_code, headers, body: HTTP_RESPONSE_BODY):
    self.status_code = status_code or 200
    self.headers     = headers
    self.body        = HTTP_RESPONSE_BODY.toJson(body)

  def _addJsonHeaders(self):
    pass

