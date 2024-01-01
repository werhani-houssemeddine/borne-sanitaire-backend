from lib.errors import ValidationError
from lib.HTTP   import HTTP_REQUEST, RESPONSE_SAMPLE

from . import AgentPermessionController

class AgentPermessionMiddleware:
  @staticmethod
  def getAgentPermessions(request: HTTP_REQUEST) -> RESPONSE_SAMPLE:
    try:
      return RESPONSE_SAMPLE.OK(AgentPermessionController.getAgentPermessions(request))
    except ValidationError as ve:
      return RESPONSE_SAMPLE.BAD_REQUEST({ str(ve.field): str(ve.message) })

  @staticmethod
  def setAgentPermession(request: HTTP_REQUEST) -> RESPONSE_SAMPLE:
    pass
  