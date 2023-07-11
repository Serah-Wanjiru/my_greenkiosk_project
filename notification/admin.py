from django.contrib import admin

# Register your models here.
from .models import Notify
class NotifyAdmin(admin.ModelAdmin):
    list_display = ('message','time','customer','types')
admin.site.register(Notify,NotifyAdmin)
