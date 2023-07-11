from django.db import models
class Payment_management(models.Model):
    amount = models.FloatField()
    payment_method = models.CharField(max_length=32)
    date = models.DateField()
    receipt = models.TextField()

    def __str__(self):
        return str(self.amount)