from django.shortcuts import render
from .models import Company

# Create your views here.

def home(request):
    return render(request, 'home.html')

def company_page(request):
    

    return render(request, 'company/detail.html',)