from django.urls import path
from . import views

urlpatterns = [
  path('login/', views.login),
  path('code-verification/', views.verify_code),
  path('check-code-verification/', views.check_verify_code),
  path('add-device/', views.addDevice)
]
