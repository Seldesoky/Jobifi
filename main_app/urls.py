from django.urls import path
from . import views 
from .views import CustomLoginView, CustomLogoutView

urlpatterns = [
    path('', views.home, name='home'),
<<<<<<< HEAD
    path('test/', views.company_page, name='company-page')
]
=======

    #Authentication
    path('accounts/register/', views.register_user, name='register_user'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', CustomLogoutView.as_view(), name='logout'),

    #Login Pages
    path('profile/job-seeker/', views.job_seeker_profile, name='job_seeker_profile'),
    path('profile/employer/', views.employer_profile, name='employer_profile'),
    ]
>>>>>>> 2665601e79a706efc91154baa37ee9c20ff8b270
