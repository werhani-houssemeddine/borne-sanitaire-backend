from lib.errors import ValidationError
from lib.HTTP   import HTTP_REQUEST

from client.Repository import NotificationPreferencesRepository, UserRepository

from client.utils import getUserId

getNotificationPreference = lambda user_id: \
  NotificationPreferencesRepository.getNotificationPreference(user_id = user_id)

class NotificationPreferencesController:
  @staticmethod
  def getNotificationPreference(request: HTTP_REQUEST):
    try:
      user_id = getUserId(request)
      notifications = getNotificationPreference(user_id)

      if request.session['__currentUser__']['role'] == "ADMIN":
        return {
          'device_configuration_change': notifications.device_configuration_change,
          'request_agent_response'     : notifications.request_agent_response,
          'agent_suspend_account'      : notifications.agent_suspend_account,
          'reached_max_visitors'       : notifications.reached_max_visitors,
          'high_max_visitors'          : notifications.hight_max_visitors
        }
      
      else:
        return {
          'reached_max_visitors': notifications.reached_max_visitors,
          'high_max_visitors'   : notifications.hight_max_visitors
        }
    
    except Exception:
      raise

  @staticmethod
  def updateNotificationPreference(request: HTTP_REQUEST):
    try:
      device_configuration_change = request.body.get('device_configuration_change')
      request_agent_response      = request.body.get('request_agent_response')
      agent_suspend_account       = request.body.get('agent_suspend_account')
      reached_max_visitors        = request.body.get('reached_max_visitors')
      high_max_visitors           = request.body.get('high_max_visitors')

      castToBoolean = lambda value: False if value == "false" else True if value == "true" else bool(value)

      print(
        castToBoolean(device_configuration_change),
        castToBoolean(request_agent_response),
        castToBoolean(agent_suspend_account),
        castToBoolean(reached_max_visitors),
        castToBoolean('false')
      )


      user = UserRepository.getUserById(getUserId(request))
      if device_configuration_change != None:
        if user.role != "ADMIN":
          raise ValidationError("UNAUTHORIZED", "CANNOT ACCESS THIS ENDPOINT")
        
        else:
          return NotificationPreferencesRepository.updateDeviceConfigurationChange(
            user_id = user.id,
            value   = castToBoolean(device_configuration_change)
          )

      if request_agent_response != None:
        if user.role != "ADMIN":
          raise ValidationError("UNAUTHORIZED", "CANNOT ACCESS THIS ENDPOINT")
        
        else: 
          return NotificationPreferencesRepository.updateRequestAgentResponse(
            user_id = user.id,
            value   = castToBoolean(device_configuration_change)
          )

      if agent_suspend_account != None:
        if user.role != "ADMIN":
          raise ValidationError("UNAUTHORIZED", "CANNOT ACCESS THIS ENDPOINT")
        
        else:
          return NotificationPreferencesRepository.updateAgentSuspendAccount(
            user_id = user.id,
            value   = castToBoolean(device_configuration_change)
          )

      if reached_max_visitors != None:
        return NotificationPreferencesRepository.updateReachedMaxVisitors(
            user_id = user.id,
            value   = castToBoolean(device_configuration_change)
          )
      
      if high_max_visitors != None:
        return NotificationPreferencesRepository.updateHightMaxVisitors(
            user_id = user.id,
            value   = castToBoolean(high_max_visitors)
          )
    
    except Exception:
      raise