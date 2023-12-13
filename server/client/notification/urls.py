from django.urls import path
from . import views

urlpatterns = [ 
  path('set-notification/', views.updateNotificationPreferences),
  path('', views.getNotificationPreferences),
]
