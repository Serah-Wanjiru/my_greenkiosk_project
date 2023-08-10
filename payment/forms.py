from django import forms
from .models import Payment_management

class PaymentAploadForm(forms.ModelForm):
    class Meta:
        model = Payment_management
        fields = '__all__'