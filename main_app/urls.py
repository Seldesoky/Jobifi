from django.urls import path
from . import views 
from .views import CustomLoginView, CustomLogoutView

urlpatterns = [
    path('', views.home, name='home'),

    #Authentication
    path('accounts/register/', views.register_user, name='register_user'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', CustomLogoutView.as_view(), name='logout'),

    #Login Pages
    path('profile/job-seeker/', views.job_seeker_profile, name='job_seeker_profile'),
    path('profile/employer/', views.employer_profile, name='employer_profile'),

    # Application-related URLs
    path('jobs/<int:id>/apply/', views.apply_for_job, name='apply_for_job'),
    path('jobs/<int:id>/applications/', views.job_applications, name='job_applications'),
    path('applications/<int:id>/', views.application_detail, name='application_detail'),
    ]
