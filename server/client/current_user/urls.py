from django.urls import path, include
from . import views

urlpatterns = [ 
  # path('', views.current),
  path('update/', include('client.current_user.update.urls')),
  path('archeive/', views.archeive)
]
