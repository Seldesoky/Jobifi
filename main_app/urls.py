from django.urls import path
from . import views 
from .views import CustomLoginView , JobUpdate, JobDelete

urlpatterns = [
    path('', views.home, name='home'),

    #Authentication
    path('accounts/register/', views.register_user, name='register_user'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),

    #Profile Pages
    path('profile/job-seeker/', views.job_seeker_profile, name='job_seeker_profile'),
    path('profile/job-seeker/edit/', views.edit_job_seeker_profile, name='edit_job_seeker_profile'),
    path('profile/employer/', views.employer_profile, name='employer_profile'),
    path('profile/employer/edit/', views.edit_employer_profile, name='edit_employer_profile'),

    
    #Job Details / Read
    path('jobs/', views.job_list, name = 'job_list'),
    path('jobs/<int:id>/', views.job_detail, name='job_detail'),

    #Job Create, Read, Delete
    path('jobs/create/', views.job_create, name='job_create'),
    path('jobs/<int:pk>/edit/', JobUpdate.as_view(), name='job_update'),
    path('jobs/<int:pk>/delete', JobDelete.as_view(), name='job_delete'),


    # Application-related URLs
    path('jobs/<int:id>/apply/', views.apply_for_job, name='apply_for_job'),
    path('jobs/<int:id>/applications/', views.job_applications, name='job_applications'),
    path('applications/<int:id>/', views.application_detail, name='application_detail'),

    # Job Search
    path('jobs/search/', views.job_search, name='job_search'),
    ]
