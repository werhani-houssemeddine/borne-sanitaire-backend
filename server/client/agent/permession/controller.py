from lib.errors import ValidationError
from lib.HTTP   import HTTP_REQUEST, RESPONSE_SAMPLE

from client.models import AgentPermessionsModel, AgentModel
from client.Repository import AgentRepository

from client.utils import getUserId

class AgentPermessionController:
  @staticmethod
  def formatPemessionResponse(permession: AgentPermessionsModel):
    return {
      'historic' : permession.check_historic,
      'config'   : permession.config_device,
      'device_id': permession.device_id.device_id
    }

  @staticmethod
  def getAgentPermessions(request: HTTP_REQUEST):
    agent_id = request.params.get('id')
    if agent_id == None: raise ValidationError('Agent', 'missing agent')
    
    user_id  = getUserId(request = request)

    try:
      agent: AgentModel = AgentRepository.getAgentById(agent_id)

      if agent.user_id.id != user_id:
        raise ValidationError('UNATHORIZED', 'AGENT ID')

      permessions = AgentPermessionsModel.objects.filter(agent_id = agent_id)

      listOfPermessions = None if permessions == None else list(
        map(AgentPermessionController.formatPemessionResponse, permessions)
      )

      return {
        'manage_devices': agent.manage_devices,
        'manage_agents' : agent.manage_agents,
        'permessions'   : listOfPermessions
      }
    
    except Exception: raise
    
  @staticmethod
  def setAgentPermession(request: HTTP_REQUEST):
    agent_id = request.params.get('id')
    if agent_id == None: return RESPONSE_SAMPLE.BAD_REQUEST({ 'agent id': 'missing agent id' })

    try:
      agent = AgentRepository.getAgentByAgentId(agent_id)
      
      if request.body.get('manage_devices') != None:
        agent.manage_devices = bool(request.body.get('manage_devices'))
        agent.save()

      elif request.body.get('manage_devices') != None:
        agent.manage_devices = bool(request.body.get('manage_devices'))
        agent.save()
      
      else:
        device_id = request.body.get('device_id')
        config_device = request.body.get('config_device')
        check_historic = request.body.get('check_historic')

        permession = AgentPermessionsModel.objects.get(agent_id = agent, device_id = device_id)
        try:
          if config_device != None:
            permession.config_device = bool(config_device)
          elif check_historic != None:
            permession.check_historic = bool(check_historic)
          
          permession.save()
        
        except AgentPermessionsModel.DoesNotExist:
          AgentPermessionsModel.objects.create(
            agent_id = agent,
            device_id = device_id,
            config_device = config_device,
            check_historic = check_historic,
          )
      
      return RESPONSE_SAMPLE.OK()
    
    except Exception:
      return RESPONSE_SAMPLE.BAD_REQUEST()
    