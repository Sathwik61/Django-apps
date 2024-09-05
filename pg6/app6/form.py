from django import forms
from .models import Students,Project

class StduentForm(forms.ModelForm):
    class Meta:
        model=Students
        fields='__all__'

class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields='__all__'