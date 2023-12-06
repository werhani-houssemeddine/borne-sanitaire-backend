
#? This file will only contains update url 

from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
  path('password/', views.updatePassword),
  path('profile-photo/', views.updateProfilePhoto),
  path('phone-number/', views.updatePhoneNumber),
  path('username/', views.updateUsername),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)