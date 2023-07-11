from django.contrib import admin
from .models import Salesperson
class SalespersonAdmin(admin.ModelAdmin):
    list_display= ('vendor_name','location','store_numb',)
admin.site.register( Salesperson, SalespersonAdmin)
