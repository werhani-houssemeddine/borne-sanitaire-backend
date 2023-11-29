from django.urls import path, include
from . import views

AGENT_ENDPOINT  = include('client.agent.urls')
ADMIN_ENDPOINT  = include('client.admin.urls')
CLIENT_ENDPOINT = include('client.current_user.urls')
DEVICE_ENDPOINT = include('client.device.urls')

urlpatterns = [ 
  path('signup/', views.signup),
  path('login/', views.login),
  # path('current-user/', views.currentUser),

  path('admin/', ADMIN_ENDPOINT),
  path('agent/', AGENT_ENDPOINT),
  path('device/', DEVICE_ENDPOINT),

  path('', CLIENT_ENDPOINT)
]
