from django.urls import path
from . import views

urlpatterns = [ 
  path('check-request-agent/<str:id>', views.checkRequestAgent),
  path('reject-request/<str:id>/', views.rejectRequestAgent)
  # path('add/', ),
  # path('edit/', ),
  # path('archieve/', ),
  # path('delete/', )  
]
