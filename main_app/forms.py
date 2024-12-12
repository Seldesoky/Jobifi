from django import forms
from .models import Application, Company, JobPosting

class JobPostingForm(forms.ModelForm):
    class Meta:
        model = JobPosting
        fields = ['title', 'description', 'company_name', 'company_description', 'location', 'salary']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['cover_letter', 'resume']


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'