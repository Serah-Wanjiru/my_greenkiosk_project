from django.shortcuts import render
from .forms import NotificationAploadForm
from .models import Notify

def upload_notify(request):
    if request.method == 'POST':
        form = NotificationAploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = NotificationAploadForm()
    return render(request, "notification/notification_upload.html", {"form": form})

