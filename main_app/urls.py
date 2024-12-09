from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),

    #Authentication
    path('accounts/register/', views.register_user, name='register_user'),
    path('accounts/login/',),
    path('accounts/sign_out',),
]
