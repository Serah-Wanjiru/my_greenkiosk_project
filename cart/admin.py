from django.contrib import admin
from .models import Basket

class BasketAdmin(admin.ModelAdmin):
    list_display = ('name', 'total', 'quantity', 'shipping_cost', 'discounts')

admin.site.register(Basket, BasketAdmin)
