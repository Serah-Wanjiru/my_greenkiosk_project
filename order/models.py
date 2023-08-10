from django.db import models
from payment.models import Payment_management
from inventory.models import Product
from customer.models import Buyer
from cart.models import Basket

class Place_order(models.Model):

    payment = models.OneToOneField(Payment_management, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=32)
    order_number = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    payment_options = models.CharField(max_length=32)
    customer = models.ForeignKey(Buyer, on_delete=models.CASCADE, null=True)
    cart= models.ManyToManyField(Basket)

    def __str__(self):
        return self.name
