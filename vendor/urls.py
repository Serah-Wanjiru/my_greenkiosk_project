from django.urls import path
from .views import upload_vendor,vendor_list,edit_vendor_view

app_name = 'vendor'

urlpatterns = [
    path('upload/',upload_vendor,name='vendor_upload_view'),
    path('list',vendor_list,name="order_list_view"),
    path('edit/<int:id>/',edit_vendor_view,name="vendor_edit_view"),
]