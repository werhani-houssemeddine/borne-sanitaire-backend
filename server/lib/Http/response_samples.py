#
  # This class will have some repsonse sample like 404, 400 ...
#
class RESPONSE_SAMPLE:
  @staticmethod
  def badRequest(details: dict = None):
    response = {
        'status_code': 400,
        'body'       : {
          'message' : 'Bad Request',
          'state'   : 'failure',
          'error'   : True,
        }
      }
    
    # Add property data if details is a dict
    if isinstance(details, dict):
      response["data"] = details
  
    return response
  
  @staticmethod
  def notFound():
    return {
      'status_code': 404,
      'body'       : {
        'message' : 'NOT FOUND',
        'state'   : 'failure',
        'error'   : True,
      }
    }
  
  @staticmethod
  def serverError():
    return {
      'status_code': 500,
      'body'       : {
        'message' : 'INTERNAL SERVER ERROR',
        'state'   : 'failure',
        'error'   : True,
      }
    }