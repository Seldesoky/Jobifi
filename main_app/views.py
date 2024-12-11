from django.shortcuts import render
from .models import Company
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

def home(request):
    return render(request, 'home.html')

def company_page(request, company_id):
    company = Company.objects.get(id=company_id)

    return render(request, 'company/detail.html', {
        'company': company,
    })

class CompanyCreate(CreateView):
    model = Company
    fields = '__all__'
    #TODO Check when im home - Possible conflict without upload functionality / logo 
    success_url = '/companies/'

class CompanyUpdate(UpdateView):
    model = Company
    fields = ['description', 'location', 'industry', 'website', 'logo']
    # everything aside from the name

class CompanyDelete(DeleteView):
    model = Company
    success_url = '/companies/'
