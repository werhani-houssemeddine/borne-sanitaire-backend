from django.urls import path
from . import views

urlpatterns = [ 
  path('check-device/', views.checkDevice),
  path('edit/', views.edit),
  path('add-agent/', views.addAgent)
]
