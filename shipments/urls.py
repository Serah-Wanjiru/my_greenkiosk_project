from django.urls import path
from .views import upload_shipment,shipments_list,edit_shipments_view

app_name = 'shipments'

urlpatterns = [
    path('upload/',upload_shipment,name='shipments_upload_view'),
    path('list',shipments_list,name="shipments_list_view"),
    path('edit/<int:id>/',edit_shipments_view,name="order_edit_view"),
]