from django.contrib import admin
from .models import Rating
class RatingAdmin(admin.ModelAdmin):
    list_display = ('message','name','product','number_of_stars','date')
admin.site.register(Rating,RatingAdmin)
