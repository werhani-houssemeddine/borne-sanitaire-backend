from django.urls import path
from . import views


urlpatterns = [ 
  path('enableOTP/', views.enableOTP),
  path('disableOTP/', views.disableOTP),
  path('checkOTP/', views.checkOTP),
]
