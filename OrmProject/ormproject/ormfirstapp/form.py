from .models import Emp
from django import forms
class EmpForm(forms.ModelForm):
    class Meta:
        model=Emp
        fields='__all__'