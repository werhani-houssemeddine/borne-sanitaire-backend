import uuid
from lib.errors import ValidationError

class UUID:
  @staticmethod
  def validateUUID(uuid_str):
    try:
      return uuid.UUID(uuid_str)
    except ValueError:
      raise ValidationError('id', 'INVALID FORMAT')