from django.urls import path, include
from . import views

AGENT_ENDPOINT  = include('client.agent.urls')
ADMIN_ENDPOINT  = include('client.admin.urls')
CLIENT_ENDPOINT = include('client.current_user.urls')
DEVICE_ENDPOINT = include('client.device.urls')

AUTHENTICATION_ENDPOINT = include('client.authentication.urls')
NOTIFICATION_ENDPOINT   = include('client.notification.urls')

urlpatterns = [ 
  path('signup/', views.signup),
  path('login/', views.login),

  path('authenticate/', AUTHENTICATION_ENDPOINT),

  # path('current-user/', views.currentUser),

  path('admin/', ADMIN_ENDPOINT),
  path('agent/', AGENT_ENDPOINT),
  path('device/', DEVICE_ENDPOINT),

  path('notification/', NOTIFICATION_ENDPOINT),

  path('', CLIENT_ENDPOINT)
]
