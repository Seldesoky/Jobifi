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
    
    path('companies/create/', views.CompanyCreate.as_view, name='company-create'),
    path('companies/<int:company_id>/', views.company_page, name='company-page'),
    path('companies/<int:pk>/edit/', views.CompanyUpdate.as_view, name='company-edit'),
    path('companies/<int:pk>/delete/', views.CompanyDelete.as_view, name='company-delete'),
    ]
# | **Companies**            | `/companies/<id>/`          | `company_detail`        |
# |                          | `/companies/create/`        | `company_create`        |
# |                          | `/companies/<id>/edit/`     | `company_edit`          |
# |                          | `/companies/<id>/delete/`   | `company_delete`        |
