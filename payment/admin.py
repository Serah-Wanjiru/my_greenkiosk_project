from django.contrib import admin

# Register your models here.
from .models import Payment_management
class Payment_managementadmin(admin.ModelAdmin):
    list_display = ('payment_method','amount','date','receipt')
admin.site.register(Payment_management,Payment_managementadmin)