from django.shortcuts import render
from .models import Company

# Create your views here.

def home(request):
    return render(request, 'home.html')

def company_page(request, company_id):
    company = Company.objects.get(id=company_id)

    return render(request, 'company/detail.html', {
        'company': company,
    })