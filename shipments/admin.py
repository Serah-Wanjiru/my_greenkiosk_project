from django.contrib import admin
from .models import Shipping
class ShippingAdmin(admin.ModelAdmin):
    list_display =('date','order','location','type_of_delivery','status')
admin.site.register(Shipping,ShippingAdmin)
