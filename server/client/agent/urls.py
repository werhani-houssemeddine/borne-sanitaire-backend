from django.urls import path
from . import views

urlpatterns = [ 
  path('check-request-agent/<str:id>', views.checkRequestAgent),
  path('reject-request/<str:id>/', views.rejectRequestAgent),
  path('agents/active/', views.getActiveAgents),
  path('agents/archeived/', views.getArcheivedAgents),
  path('agents/pending/', views.gentPendingAgents),
  path('agents/', views.getAllAgents),
  path('agent/<str:id>', views.getOneAgentData)
  # path('add/', ),
  # path('edit/', ),
  # path('archieve/', ),
  # path('delete/', )  
]
