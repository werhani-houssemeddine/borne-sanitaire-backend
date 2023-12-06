from lib.HTTP import HTTP_REQUEST, RESPONSE_SAMPLE

from client.current_user.Controller import UserController, ValidateUserData
from .update_user_middleware        import UpdateUserMiddleware

from client.Repository import UserRepository 

class UserMiddleware(UpdateUserMiddleware):
  @staticmethod
  def getCurrentUser(request: HTTP_REQUEST):
    response = UserController(request)
    return RESPONSE_SAMPLE.OK(
      data = response.toJSON()
    )
  
  #? This endpoint returns true if the phone number does not exist 
  #? this will be used to verify if the client can use this phone number

  @staticmethod
  def checkPhoneNumber(request: HTTP_REQUEST):
    phone_number = request.params.get('phone')
    if ValidateUserData.validatePhoneNumber(phone_number):
        if UserRepository.getUserByPhoneNumber(phone_number) == None:
          return RESPONSE_SAMPLE.OK()
        else:
          return RESPONSE_SAMPLE.NOT_FOUND()

    else:
      return RESPONSE_SAMPLE.BAD_REQUEST({'phone_number': 'Invalid format'})
      
