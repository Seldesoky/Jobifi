from django.urls import path
from . import views 
from .views import CustomLoginView, CustomLogoutView

urlpatterns = [
    path('', views.home, name='home'),

    #Authentication
    path('accounts/register/', views.register_user, name='register_user'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', CustomLogoutView.as_view(), name='logout'),
    ]
