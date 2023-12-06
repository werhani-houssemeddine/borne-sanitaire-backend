from django.urls import path, include
from . import views

urlpatterns = [ 
  path('', views.current),
  path('check-phone/<str:phone>', views.check_phoneNumber),
  path('update/', include('client.current_user.update.urls')),
  path('archeive/', views.archeive)
]
