#
  # This class will have some repsonse sample like 404, 400 ...
#
class RESPONSE_SAMPLE:
  @staticmethod
  def badRequest(details: dict):
    
    if isinstance(details, dict) == False:
      return {
        'status_code': 400,
        'body'       : {
          'message' : 'Bad Request',
          'state'   : 'failure',
          'error'   : True,
        }
      }
  
    else:
      return {
      'status_code': 400,
        'body'       : {
          'message' : 'Bad Request',
          'state'   : 'failure',
          'error'   : True,
        }
      }