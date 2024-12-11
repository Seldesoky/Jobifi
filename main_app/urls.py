from django.urls import path
from . import views 
from .views import CustomLoginView

urlpatterns = [
    path('', views.home, name='home'),

    #Authentication
    path('accounts/register/', views.register_user, name='register_user'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),


    #Login Pages
    path('profile/job-seeker/', views.job_seeker_profile, name='job_seeker_profile'),
    path('profile/employer/', views.employer_profile, name='employer_profile'),
    
    #Job Details / Read
    path('jobs/', views.job_list, name = 'job_list'),
    path('jobs/<int:id>/', views.job_detail, name='job_detail'),

    #Job Create, Read, Delete
    path('jobs/create/', views.job_create, name='job_create'),
    path('jobs/<int:id>/edit', views.job_edit, name='job_edit'),
    path('jobs/<int:id>/delete', views.job_delete, name='job_delete'),
    ]
