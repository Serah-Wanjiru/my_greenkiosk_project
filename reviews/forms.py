from django import forms
from .models import Rating

class ReviewAploadForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = '__all__'