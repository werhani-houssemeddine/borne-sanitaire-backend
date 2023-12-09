from client.models import UserPictureModel

class UserPictureRepository:
  @staticmethod
  def getUserPicture(user_id) -> UserPictureModel | None:
    try:
      return UserPictureModel.objects.get(user_id = user_id)
    
    except UserPictureModel.DoesNotExist:
      return None