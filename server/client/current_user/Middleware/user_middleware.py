from lib.HTTP import HTTP_REQUEST, RESPONSE_SAMPLE

from client.current_user.Controller import UserController

from .update_user_middleware import UpdateUserMiddleware
class UserMiddleware(UpdateUserMiddleware):
  @staticmethod
  def getCurrentUser(request: HTTP_REQUEST):
    response = UserController(request)
    return RESPONSE_SAMPLE.OK(
      data = response.toJSON()
    )
  