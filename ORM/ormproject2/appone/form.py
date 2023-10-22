from .models import Manual
from django import forms

class AutoForm(forms.ModelForm):
    class Meta:
        model=Manual
        fields='__all__'