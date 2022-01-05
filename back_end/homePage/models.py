from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Sale(models.Model):
    saleID = models.AutoField(primary_key=True)
    typeOf = models.IntegerField(validators=[MaxValueValidator(6), MinValueValidator(0),])
    salePercentage = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0),])
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
