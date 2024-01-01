from django.urls import path, include
from . import views

urlpatterns = [ 
  path('get/<str:id>/', views.getPermessions),
  path('set/<str:id>/', views.setPermessions)
]
