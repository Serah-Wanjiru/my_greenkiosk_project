from django import forms
from .models import Buyer

class CustomerAploadForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = '__all__'