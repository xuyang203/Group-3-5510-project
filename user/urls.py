from django.urls import path
from . import views

urlpatterns =[
    path('reg',views.reg_view),
    path('log',views.log_view),
    path('logout',views.logout_view),
]