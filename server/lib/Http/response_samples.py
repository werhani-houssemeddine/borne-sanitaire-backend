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
      response["body"]["data"] = details

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
  
  @staticmethod
  def successfullyCreadted(details: dict = None):
    response = {
      'status_code': 201,
      'body'       : {
        'message': 'CREATED SUCCESSFULLY',
        'state'  : 'SUCCESS',
        'error'  : False,
      }
    }

    if isinstance(details, dict):
      response['body']['data'] = details

    return response
  
  @staticmethod
  def notAuthorised():
    return {
      'status_code': 401,
      'body'       : {
        'message': 'UNAUTHORISED',
        'state'  : 'failure',
        'error'  : True,
      }
    }
  
  @staticmethod
  def ok(data = None):
    response = {
      'status_code': 200,
      'body'       : {
        'message': 'OK',
        'state'  : 'success',
        'error'  : False,
      }
    }

    if data != None:
      response['body']['data'] = data

    return response