from lib.errors import ValidationError
from lib.HTTP   import HTTP_REQUEST, RESPONSE_SAMPLE

from client.current_user.Controller import UpdateUserController

from client.Repository import UserRepository
from client.models     import UserPictureModel

from time import time

class UpdateUserMiddleware:
  @staticmethod
  def updateUsername(request: HTTP_REQUEST):
    try:
      update = UpdateUserController(request)
      if update.updateUsername():
        return RESPONSE_SAMPLE.OK({ 'username': 'updated successfully' })
    
    except ValidationError as ve:
      return RESPONSE_SAMPLE.BAD_REQUEST({ str(ve.field): str(ve.message) })
    except Exception:
      return RESPONSE_SAMPLE.BAD_REQUEST()

  @staticmethod
  def updatePassword(request: HTTP_REQUEST):
    try:
      update = UpdateUserController(request)
      if update.updatePassword():
        return RESPONSE_SAMPLE.OK({ 'password': 'updated successfully' })

    except ValidationError as ve:
      print(ve)
      return RESPONSE_SAMPLE.BAD_REQUEST({ str(ve.field): str(ve.message) })
    except Exception as e:
      return RESPONSE_SAMPLE.BAD_REQUEST()

  @staticmethod
  def updatePhoneNumber(request: HTTP_REQUEST):
    try:
      update = UpdateUserController(request)
      if update.updatePhoneNumber():
        return RESPONSE_SAMPLE.OK({ 'phone_number': 'updated successfully' })
    
    except ValidationError as ve:
      return RESPONSE_SAMPLE.BAD_REQUEST({ str(ve.field): str(ve.message) })
    except Exception:
      return RESPONSE_SAMPLE.BAD_REQUEST()
    
  @staticmethod
  def updateProfilePhoto(request: HTTP_REQUEST):
    try:
      update  = UpdateUserController(request)
      user_id = update.user_id
      picture = request.body.get('picture')

      current_timestamp = int(time())
      pictureModel      = UserPictureModel()

      picture_extension = '.' + picture.name.split(".")[-1]

      picture.name = str(current_timestamp) + '_' + str(user_id) + picture_extension

      pictureModel.user_id = UserRepository.getUserById(user_id)
      pictureModel.avatar  = request.body.get('picture')

      pictureModel.save()

      return RESPONSE_SAMPLE.CREATED({'profile photo': 'updated_successfully'})


    except ValidationError as ve:
      return RESPONSE_SAMPLE.BAD_REQUEST({ str(ve.field): str(ve.message) })
    except Exception as e:
      print(e)
      return RESPONSE_SAMPLE.BAD_REQUEST()
    