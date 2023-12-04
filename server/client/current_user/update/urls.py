
#? This file will only contains update url 

from django.urls import path
from . import views

urlpatterns = [ 
  path('password/', views.updatePassword),
  path('profile-photo/', views.updateProfilePhoto),
  path('phone-number/', views.updatePhoneNumber),
  path('username/', views.updateUsername),
]
