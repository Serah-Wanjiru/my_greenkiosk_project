from django.contrib import admin
from .models import Buyer
class BuyerAdmin(admin.ModelAdmin):
    list_display=('id','name', 'contacts','location','email_adress')
admin.site.register(Buyer,BuyerAdmin)

