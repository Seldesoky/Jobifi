from django import forms
from .models import JobPosting

class JobPostingForm(forms.ModelForm):
    class Meta:
        model = JobPosting
        fields = ['title', 'description', 'company', 'location', 'salary']