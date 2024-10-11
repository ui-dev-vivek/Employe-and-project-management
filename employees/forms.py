from django import forms
from .models import Employees



class EmployeeAdminForm(forms.ModelForm):
    class Meta:
        model=Employees
        fielsd='__all__'
    