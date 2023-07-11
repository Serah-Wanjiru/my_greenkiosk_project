from django.contrib import admin
from .models import Place_order
class Place_orderAdmin(admin.ModelAdmin):
    list_display = ('name','total', 'order_number','date')
admin.site.register(Place_order,Place_orderAdmin)