from django import forms
from .models import Salesdata

class SalesdataForm(forms.ModelForm):
    class Meta:
        model = Salesdata
        fields = '__all__'