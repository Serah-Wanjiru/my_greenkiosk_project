from django.urls import path
from .views import upload_notify

urlpatterns=[path('upload/', upload_notify, name='notification_upload_view'),
             
             ]