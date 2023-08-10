from django.urls import path
from .views import upload_customer,customer_list

urlpatterns=[path("upload/",upload_customer,name="customer_upload_view"),
             path('list',customer_list,name="customer_list_view"),
             ]
