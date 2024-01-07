from django.urls import path, include
from . import views

urlpatterns = [ 
  path('check-request-agent/', views.checkRequestAgent),
  path('reject-request/<str:id>/', views.rejectRequestAgent),
  path('active/', views.getActiveAgents),
  path('archeived/', views.getArcheivedAgents),
  path('pending/', views.gentPendingAgents),
  path('all/', views.getAllAgents),
  path('one/<int:id>/', views.getOneAgentData),

  path('permession/', include('client.agent.permession.urls')),
  # path('add/', ),
  # path('edit/', ),
  path('archieve/<int:id>/', views.archieveAgent),
  path('dearchive/<int:id>/', views.dearchieveAgent),
  path('delete/<int:id>/', views.deleteAgent)  
]
