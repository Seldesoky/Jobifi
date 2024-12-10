from django.urls import path
from . import views 
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),

    #Authentication
    path('accounts/register/', views.register_user, name='register_user'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    ]
