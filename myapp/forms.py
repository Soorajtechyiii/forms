from django import forms
from .models import Employee

class Employeeforms(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
        