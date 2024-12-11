from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('companies/create/', views.company_create, name='company-create')
    path('companies/<int:company_id>/', views.company_page, name='company-page')
    path('companies/<int:pk>/edit/', views.company_edit, name='company-edit')
    path('companies/<int:pk>/delete/', views.company_delete, name='company-delete')
]
# | **Companies**            | `/companies/<id>/`          | `company_detail`        |
# |                          | `/companies/create/`        | `company_create`        |
# |                          | `/companies/<id>/edit/`     | `company_edit`          |
# |                          | `/companies/<id>/delete/`   | `company_delete`        |