from django.urls import path, include
from . import views

urlpatterns = [ 
  path('check-device/', views.checkDeviceAvailability)
]
