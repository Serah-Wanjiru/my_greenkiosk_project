from django.urls import path
from .views import upload_cart,cart_list,edit_cart_view

urlpatterns=[path("upload/",upload_cart,name="cart_upload_view"),
             path('list',cart_list,name="cart_list_view"),
             path('edit/<int:id>/',edit_cart_view,name="order_edit_view"),
             
             ]

