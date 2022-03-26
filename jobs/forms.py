from django import forms
from .models import Job

class JobCreationForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ['recruiter', 'applicants']