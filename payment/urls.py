from django.urls import path
from .views import upload_pay

app_name = 'payment'

urlpatterns = [
    path('upload/', upload_pay, name='payment_upload_view'),
    
]