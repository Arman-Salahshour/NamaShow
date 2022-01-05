from django.db import models
from Login.models import User

# Create your models here.


class Payment(models.Model):
    trackingCode = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    dateOf = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return f"{self.userID}: {self.amount}IRR, {self.trackingCode}"