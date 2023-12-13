from client.models import UserPictureModel

class UserPictureRepository:
  @staticmethod
  def getUserPicture(user_id) -> UserPictureModel | None:
    try:
      return UserPictureModel.objects.get(user_id = user_id)
    
    except UserPictureModel.DoesNotExist:
      return None
  
  @staticmethod
  def deletePictureByUserId(user_id):
    try:
      user_picture = UserPictureRepository.getUserPicture(user_id)
      if user_picture != None:
        user_picture.delete()
      
    except Exception:
      raise