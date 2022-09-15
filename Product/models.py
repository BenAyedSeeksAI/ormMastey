from django.db import models

# Create your models here.
class product(models.Model):
    uid = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    def __str__(self) -> str:
        return f"{self.name} has the price of {self.price}"
     

