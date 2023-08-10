from django import forms
from .models import Place_order

class OrderAploadForm(forms.ModelForm):
    class Meta:
        model = Place_order
        fields = '__all__'