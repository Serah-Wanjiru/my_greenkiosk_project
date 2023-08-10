from django import forms
from .models import Salesperson

class VendorAploadForm(forms.ModelForm):
    class Meta:
        model = Salesperson
        fields = '__all__'