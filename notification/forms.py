from django import forms
from .models import Notify

class NotificationAploadForm(forms.ModelForm):
      class Meta:
              model=Notify
              fields= "__all__"