from django import forms
from .models import Application, Company

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['cover_letter', 'resume']


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'