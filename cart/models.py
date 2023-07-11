from django.db import models
from inventory.models import Product
class Basket(models.Model):
    products = models.ManyToManyField(Product)
    name=models.CharField(max_length=32)
    total = models.IntegerField()
    quantity = models.IntegerField()
    shipping_cost = models.FloatField()
    discounts = models.FloatField()

    def __str__(self):
        return self.name
