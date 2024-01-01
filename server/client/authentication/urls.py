from django.urls import path
from . import views


urlpatterns = [ 
  path('signup-email/', views.signupEmail),
  path('check-singup-code/', views.checkSignupCode),
  path('check-login-code/', views.checkLoginCode),
  path('enableOTP/', views.enableOTP),
  path('disableOTP/', views.disableOTP),
  path('checkOTP/', views.checkOTP),
  path('delete/account/', views.deleteAccount)
]
