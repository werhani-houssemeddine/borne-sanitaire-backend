from django.urls import path
from . import views

urlpatterns = [ 
  path('current-user/', views.currentUser),
  path('edit/', views.edit),
]