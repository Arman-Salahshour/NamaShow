from django.db import models
from Login.models import User

# Create your models here.


class Subscription(models.Model):
    subID = models.AutoField(primary_key=True)
    nameOf = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    salePercentage = models.PositiveIntegerField(default=0)
    saleExpiration = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nameOf}: {self.price}IRR"


class SubPurchase(models.Model):
    price = models.PositiveIntegerField()
    dateOf = models.DateTimeField(auto_now_add=True)
    
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    subscription = models.ForeignKey(Subscription, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.subscription