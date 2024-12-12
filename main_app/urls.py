from django.urls import path
from . import views 
from .views import CustomLoginView, CustomLogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('companies/create/', views.CompanyCreate.as_view, name='company-create'),
    path('companies/<int:company_id>/', views.company_page, name='company-page'),
    path('companies/<int:pk>/edit/', views.CompanyUpdate.as_view, name='company-edit'),
    path('companies/<int:pk>/delete/', views.CompanyDelete.as_view, name='company-delete'),
]
# | **Companies**            | `/companies/<id>/`          | `company_detail`        |
# |                          | `/companies/create/`        | `company_create`        |
# |                          | `/companies/<id>/edit/`     | `company_edit`          |
# |                          | `/companies/<id>/delete/`   | `company_delete`        |
