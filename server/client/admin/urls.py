from django.urls import path
from . import views

urlpatterns = [ 
  path('check-device/', views.checkDevice),
  path('edit/', views.edit),
  path('add-agent/', views.addAgent),
  path('request/all/', views.getAllRequestAgent),
  path('request/one/<str:id>/', views.getSingleRequestAgent),
  path('request/delete/<str:id>/', views.deleteRequestAgent)
]
