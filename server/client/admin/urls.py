from django.urls import path
from . import views

urlpatterns = [ 
  path('edit/', views.edit),
  path('add-agent/', views.addAgent)
]
