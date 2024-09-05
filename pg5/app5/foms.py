from django import forms
from .models import Students, Cources

class StudentForm(forms.ModelForm):
    class Meta:
        model=Students
        fields=['name','email','cources']
        # widgets = {
        #     'courses': forms.SelectMultiple(attrs={'class': 'form-control'})
        # }


class CourceForm(forms.ModelForm):
    class Meta:
        model=Cources
        fields='__all__'