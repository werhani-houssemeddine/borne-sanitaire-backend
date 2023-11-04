from django.urls import path
from . import views

urlpatterns = [
  path('', views.completeRequest),
  path('reject-request/', views.rejectRequest)
]
