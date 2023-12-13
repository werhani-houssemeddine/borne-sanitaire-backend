from rest_framework.decorators import api_view

from lib.make_request                 import makeRequest
from lib.utils                        import Authenticate

from client.notification.Middleware import NotificationPreferencesMiddleware

@api_view(['GET'])
@Authenticate
def getNotificationPreferences(request):
    return makeRequest(
      request = request, 
      middleware = NotificationPreferencesMiddleware.getNotificationPreferences
    )

@api_view(['PUT'])
@Authenticate
def updateNotificationPreferences(request):
    return makeRequest(
      request    = request,
      middleware = NotificationPreferencesMiddleware.updateNotificationPreferences
    )
