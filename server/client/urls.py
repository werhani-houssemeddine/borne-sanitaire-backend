from django.urls import path, include
from . import views

AGENT_ENDPOINT = include('client.agent.urls')
USER_ENDPOINT  = include('client.user.urls')

urlpatterns = [ 
  path('signup/', views.signup),
  path('login/', views.login),

  path('user/', USER_ENDPOINT),
  path('agent/', AGENT_ENDPOINT)
]
