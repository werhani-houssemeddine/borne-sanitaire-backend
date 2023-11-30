from django.urls import path
from . import views

urlpatterns = [ 
  path('check-request-agent/', views.checkRequestAgent),
  path('reject-request/<str:id>/', views.rejectRequestAgent),
  path('active/', views.getActiveAgents),
  path('archeived/', views.getArcheivedAgents),
  path('pending/', views.gentPendingAgents),
  path('all/', views.getAllAgents),
  path('one/<int:id>/', views.getOneAgentData)
  # path('add/', ),
  # path('edit/', ),
  # path('archieve/', ),
  # path('delete/', )  
]
