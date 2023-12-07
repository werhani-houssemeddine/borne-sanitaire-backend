from django.urls import path, include
from . import views

urlpatterns = [ 
  path('check-device/', views.checkDeviceAvailability),
  path('visitor/<str:device>', views.visitors),
  path('all/', views.getAllDevices),
  path('<str:device>/', views.getOneDevice),
]
