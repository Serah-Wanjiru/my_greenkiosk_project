from django.db import models
from django.contrib.auth.models import User
class Buyer(models.Model):
   user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
   name = models.CharField(max_length=16)
   email_adress= models.CharField(max_length=16)
   location = models.CharField(max_length=32)
   contacts= models.PositiveBigIntegerField()
    
   def __str__(self):
        return self.name
