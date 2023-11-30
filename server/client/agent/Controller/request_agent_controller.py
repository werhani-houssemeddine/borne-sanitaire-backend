import uuid

from lib.errors import ValidationError
from lib.HTTP   import HTTP_REQUEST

from client.Repository import RequestAgentRepository

def validateUUID(uuid_str):
  try:
    return uuid.UUID(uuid_str)
  except ValueError:
    raise ValidationError('id', 'INVALID FORMAT')

class RequestAgentController:
  @staticmethod
  def reject(request: HTTP_REQUEST) -> bool:
    try:
      request_id = validateUUID(request.params.get('id'))

      if request_id is not None:
        return RequestAgentRepository.updateRequestAgentState(request_id, 'REJECT')

      raise ValidationError('REQUEST', 'REQUIRED REQUEST ID')
      
    except ValidationError: raise
    except Exception: raise
  
  @staticmethod
  def checkExistRequestAgent(request: HTTP_REQUEST) -> bool:
    try:
      request_id = validateUUID(request.query.get('agent'))
      request_agent = RequestAgentRepository.getPendingRequestAgentById(request_id)
      return request_agent is not None
    except Exception:
      return False