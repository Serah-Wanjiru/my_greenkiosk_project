from django.db import models


class Salesperson(models.Model):
    vendor_name = models.CharField(max_length=32)
    location = models.TextField()
    store_numb = models.CharField(max_length = 32)
   

    def __str__(self):
        return self.vendor_name
