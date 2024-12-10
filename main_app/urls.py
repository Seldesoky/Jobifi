from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('co/<str:company_name>', views.company_page, name='company-page')
]
