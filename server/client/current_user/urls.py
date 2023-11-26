from django.urls import path, include
from . import views

urlpatterns = [ 
  path('', views.current),
  path('update/', views.update),
  path('archeive/', views.archeive)
]
