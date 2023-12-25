from lib.errors import ValidationError

from client.models import NotificationPreferencesModel, UserModel

from client.Repository import UserRepository


class NotificationPreferencesRepository:
  @staticmethod
  def initAdminNotification(admin: UserModel) -> NotificationPreferencesModel:
    try:
      return NotificationPreferencesModel.objects.create(
        user_id = admin,
        agent_suspend_account = True,
        device_configuration_change = True,
        request_agent_response = True,
        reached_max_visitors = True,
        high_max_visitors = True
      )
    except Exception: raise

  @staticmethod
  def initAgentNotification(agent: UserModel) -> NotificationPreferencesModel:
    try:
      return NotificationPreferencesModel.objects.create(user_id = agent)
    except Exception: raise

  @staticmethod
  def getNotificationPreference(user_id):
    try:
      return NotificationPreferencesModel.objects.get(user_id = user_id)
    
    except NotificationPreferencesModel.DoesNotExist:
      raise ValidationError(field = 'user', message = 'Invalid User')
    except Exception: raise

  @staticmethod
  def _update_preference_field(user_id, field_name, value):
    try:
      preferences = NotificationPreferencesModel.objects.get(user_id=user_id)
      setattr(preferences, field_name, value)
      preferences.save()
      return preferences

    except NotificationPreferencesModel.DoesNotExist:
      raise ValidationError(field='user', message='Invalid User')
    except Exception as e:
      raise e

  @staticmethod
  def updateAgentSuspendAccount(user_id, value):
    NotificationPreferencesRepository._update_preference_field(user_id, 'agent_suspend_account', value)
    return True

  @staticmethod
  def updateDeviceConfigurationChange(user_id, value):
    NotificationPreferencesRepository._update_preference_field(user_id, 'device_configuration_change', value)
    return True

  @staticmethod
  def updateRequestAgentResponse(user_id, value):
    NotificationPreferencesRepository._update_preference_field(user_id, 'request_agent_response', value)
    return True

  @staticmethod
  def updateReachedMaxVisitors(user_id, value):
    NotificationPreferencesRepository._update_preference_field(user_id, 'reached_max_visitors', value)
    return True

  @staticmethod
  def updateHightMaxVisitors(user_id, value):
    NotificationPreferencesRepository._update_preference_field(user_id, 'high_max_visitors', value)
    return True

  @staticmethod
  def deleteNotificationPreferences(user_id):
    try:
      return NotificationPreferencesModel.objects.get(user_id=user_id).delete()[0]

    except Exception as e:
      raise e
