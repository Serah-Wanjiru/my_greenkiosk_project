from django.urls import path
from .views import upload_reviews

app_name = 'reviews'

urlpatterns = [
    path('upload/', upload_reviews,name='order_upload_view'),
 
]