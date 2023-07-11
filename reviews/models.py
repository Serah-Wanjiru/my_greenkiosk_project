from django.db import models
class Rating(models.Model):
    name=models.CharField(max_length=32)
    message = models.TextField()
    product = models.TextField()
    number_of_stars = models.IntegerField()
    date = models.DateField()
    
    def __str__(self):
        return  self.name
